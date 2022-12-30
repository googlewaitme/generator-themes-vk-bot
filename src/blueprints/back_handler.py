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


back_router = DefaultRouter()

fsm = FiniteStateMachine()


@simple_bot_message_handler(back_router, CommandsFilter("menu"))
async def back_in_menu(event: SimpleBotEvent):
	user = event['current_user']
	if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
		await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
	return await event.answer(
		message=messages.START_MESSAGE.format(name=user.first_name),
		keyboard=MENU_KB.get_keyboard(),
	)


@simple_bot_message_handler(back_router, CommandsFilter("back"))
async def back_in_menu(event: SimpleBotEvent):
	user = event['current_user']
	if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
		await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
	return await event.answer(
		message=messages.START_MESSAGE.format(name=user.first_name),
		keyboard=MENU_KB.get_keyboard(),
	)
