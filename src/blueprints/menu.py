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


fsm = FiniteStateMachine()
menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router)
async def send_menu(event: SimpleBotEvent) -> str:
    user = event['current_user']
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    await event.answer(
        message=messages.START_MESSAGE.format(name=user.first_name),
        keyboard=MENU_KB.get_keyboard()
    )
