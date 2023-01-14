import typing
from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult

from datetime import timedelta


class SpamControlMiddleware(BaseMiddleware):
    def __init__(self, spam_controller):
        self.spam_controller = spam_controller

    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        user_id = event.object.object.message.from_id
        one_hour_delta = timedelta(hours=1)

        if self.spam_controller.exists(user_id):
            count_of_messages_per_hour = self.spam_controller.incr(user_id)
        else:
            count_of_messages_per_hour = self.spam_controller.setex(user_id, one_hour_delta, value=1)

        if count_of_messages_per_hour > config.LIMIT_NUMBER_OF_MESSAGES_PER_HOUR:
            self.generate_captcha(user_id)
            await event.api_ctx.messages.send(
                user_id=user_id, random_id=0, message="Введите ответ:\n" + self.captcha_question)
            self.spam_controller.set(self.captcha_key, value=self.captcha_answer)
            logging.info(f"user{user_id} in ban")
            return MiddlewareResult(False)
        return MiddlewareResult(True)
