from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    CommandsFilter,
)
import messages


referal_system_router = DefaultRouter()


@simple_bot_message_handler(
    referal_system_router,
    CommandsFilter("get_ref_url"))
async def send_user_referal_url(event: SimpleBotEvent) -> str:
    user = event['current_user']
    api = event.api_ctx
    url = messages.REFERAL_URL_TEMPLATE.format(
        ref=f"user_id:{user.user_id}",
        ref_source="vkbot:shortlink"
    )
    response = await api.utils.get_short_link(url=url)
    url = response.response.short_url
    text_message = messages.MESSAGE_WITH_REFERAL_URL_TEMP.format(url=url)
    return await event.answer(text_message)
