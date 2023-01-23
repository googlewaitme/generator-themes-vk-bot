from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult

from db.models import User
from datetime import datetime


class UserMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        user_id = event['user_id']

        user = User.get_or_none(User.user_id == user_id)

        if user is None:
            user_data = await event.api_ctx.users.get(user_ids=user_id)
            user = User.create(
                user_id=user_id,
                first_name=user_data.response[0].first_name,
                loggin_date=datetime.now(),
                registration_date=datetime.now()
            )
        else:
            user.loggin_date = datetime.now()
            user.save()

        event["current_user"] = user
        return MiddlewareResult(True)
