from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult


class ReferalSystemMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        message = event.object.object.message
        if message.ref is not None:
            user = event['current_user']
            if user.referal_code is None:
                user.referal_code = message.ref
                user.save()
        return MiddlewareResult(True)
