from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
from vkwave.types.bot_events import BotEventType


class ReferalSystemMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        # TODO ref for every type of messages
        if event.object.type != BotEventType.MESSAGE_NEW:
            return MiddlewareResult(True)
        message = event.object.object.message
        if message.ref is not None:
            user = event['current_user']
            if user.referal_code is None:
                user.referal_code = message.ref
                user.referal_source = message.ref_source
                user.save()
        return MiddlewareResult(True)
