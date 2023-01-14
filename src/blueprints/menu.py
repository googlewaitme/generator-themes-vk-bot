from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    PayloadFilter,
    FiniteStateMachine,
    State,
    ForWhat,
    StateFilter,
    CommandsFilter,
    Keyboard,
)
from utils.constants import MENU_KB
import messages


menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router)
async def send_request(event: SimpleBotEvent) -> str:
    user = event['current_user']
    await event.answer(
        message=messages.START_MESSAGE.format(name=user.first_name),
        keyboard=MENU_KB.get_keyboard()
    )
