import json
import random

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

from db.models import User
from utils.constants import MENU_KB
from loader import dv
import messages

new_content_plan_router = DefaultRouter()

fsm = FiniteStateMachine()


class CoinState:
	user_input = State("input")


@simple_bot_message_handler(new_content_plan_router, PayloadFilter({"command": "create_content_plan"}))
async def start_coin_flip(event: SimpleBotEvent):
	await fsm.set_state(event=event, state=CoinState.user_input, for_what=ForWhat.FOR_USER)
	return await event.answer(
		message=messages.GETTING_THEME_TO_CONTENT_PLAN,
		keyboard=Keyboard.get_empty_keyboard(),
	)


@simple_bot_message_handler(
	new_content_plan_router,
	StateFilter(fsm=fsm, state=CoinState.user_input, for_what=ForWhat.FOR_USER),
)
async def send_generated_article(event: SimpleBotEvent):
	user: User = event["current_user"]
	text = event.object.object.message.text
	if not text:
		return await event.answer(message="Необходимо ввести текст")
	await event.answer(messages.WAITING_RESULT_MESSAGE)
	answer = dv.get_content_plan_by_theme(event.object.object.message.text)
	return await event.answer(answer, keyboard=MENU_KB.get_keyboard())

