import logging
from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult

from datetime import timedelta

import messages
import config

import random


class SpamControlMiddleware(BaseMiddleware):
    def __init__(self, spam_controller):
        # spam_controller is redis database
        self.spam_controller = spam_controller
        self.OPERATIONS = (
            ("+", lambda x, y: x + y),
            ("-", lambda x, y: x - y),
            ("*", lambda x, y: x * y)
        )
        self.MIN_INT = 0
        self.MAX_INT = 10
        self.one_hour_delta = timedelta(hours=1)

    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        self.event = event
        self.user_id = event['user_id']
        self.message_text = event.object.object.message.text
        self.captcha_key = "captcha_" + str(self.user_id)

        if self.spam_controller.exists(self.captcha_key):
            return await self.check_captcha()

        if not self.spam_controller.exists(self.user_id):
            self.spam_controller.setex(
                self.user_id, self.one_hour_delta, value=0)
        count_messages_per_hour = self.spam_controller.incr(self.user_id)

        if count_messages_per_hour > config.LIMIT_NUMBER_OF_MESSAGES_PER_HOUR:
            await self.send_captcha()
            logging.info(f"user{self.user_id} in ban")
            return MiddlewareResult(False)
        return MiddlewareResult(True)

    async def check_captcha(self):
        right_answer = self.spam_controller.get(self.captcha_key)
        if not self.message_text.isdigit():
            await self.send_captcha()
            return MiddlewareResult(False)
        if int(self.message_text) != int(right_answer):
            await self.send_captcha()
            return MiddlewareResult(False)
        self.spam_controller.setex(
            self.user_id, self.one_hour_delta, value=0)
        self.spam_controller.delete(self.captcha_key)
        await self.send_message(messages.CAPTCHA_IS_RIGHT)
        return MiddlewareResult(True)

    async def send_captcha(self):
        self.generate_captcha()
        text_message = messages.CAPTCHA_QUESTION.format(self.captcha_question)
        await self.send_message(text_message)
        self.spam_controller.set(self.captcha_key, value=self.captcha_answer)

    def generate_captcha(self):
        symbol_operation, operation = random.choice(self.OPERATIONS)

        a = random.randint(self.MIN_INT, self.MAX_INT)
        b = random.randint(self.MIN_INT, a)

        self.captcha_question = messages.CAPTCHA_TEMPLATE.format(
            first_value=a,
            second_value=b,
            operation=symbol_operation)
        self.captcha_answer = operation(a, b)

    async def send_message(self, text_message):
        await self.event.api_ctx.messages.send(
            user_id=self.user_id, random_id=0, message=text_message)
