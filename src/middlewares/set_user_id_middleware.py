from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult
from vkwave.types.bot_events import BotEventType


class SetUserIDMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        object_type = event.object.type
        if object_type == BotEventType.MESSAGE_NEW:
            user_id = event.object.object.message.from_id
        elif object_type == BotEventType.VKPAY_TRANSACTION:
            user_id = event.object.object.from_id
        event['user_id'] = user_id
        return MiddlewareResult(True)
