from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    FiniteStateMachine,
    ForWhat,
    CommandsFilter,
)
from utils.constants import MENU_KB
import messages


back_router = DefaultRouter()

fsm = FiniteStateMachine()


@simple_bot_message_handler(back_router, CommandsFilter("menu"))
async def back_in_menu(event: SimpleBotEvent):
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=messages.MAIN_MENU_TEXT,
        keyboard=MENU_KB.get_keyboard(),
    )


@simple_bot_message_handler(back_router, CommandsFilter("back"))
async def back_handler(event: SimpleBotEvent):
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=messages.MAIN_MENU_TEXT,
        keyboard=MENU_KB.get_keyboard(),
    )
