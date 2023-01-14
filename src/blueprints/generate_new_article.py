import json

from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    PayloadFilter,
    FiniteStateMachine,
    State,
    ForWhat,
    StateFilter,
    PayloadContainsFilter,
    Keyboard,
)

from utils.generate_keyboard import get_key_for_skills
from loader import dv
import messages

new_article_router = DefaultRouter()

fsm = FiniteStateMachine()


class CoinState:
    user_input = State("input")


@simple_bot_message_handler(
    new_article_router, PayloadFilter({"command": "create_article"}))
async def start_coin_flip(event: SimpleBotEvent):
    await fsm.set_state(
        event=event, state=CoinState.user_input, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=messages.GETTING_THEME_TO_ARTICLE,
        keyboard=Keyboard.get_empty_keyboard(),
    )


@simple_bot_message_handler(
    new_article_router,
    StateFilter(fsm=fsm, state=CoinState.user_input, for_what=ForWhat.FOR_USER)
)
async def send_generated_article(event: SimpleBotEvent):
    theme = event.object.object.message.text
    if not theme:
        return await event.answer(message="Необходимо ввести текст")
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    answer = dv.get_atricle_by_theme(theme)
    generated_keyboard = get_key_for_skills(
        button_again_name=messages.NEW_ARTICLE_BACK_BUTTON,
        payload={"new_article": theme})
    await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        answer, keyboard=generated_keyboard.get_keyboard())


@simple_bot_message_handler(
    new_article_router,
    PayloadContainsFilter("new_article"))
async def send_new_article_by_old_theme(event: SimpleBotEvent):
    raw_payload = event.object.object.message.payload
    payload = json.loads(raw_payload)
    theme = payload['new_article']
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    answer = dv.get_atricle_by_theme(theme)
    generated_keyboard = get_key_for_skills(
        button_again_name=messages.NEW_ARTICLE_BACK_BUTTON,
        payload={"new_article": theme})
    return await event.answer(
        answer, keyboard=generated_keyboard.get_keyboard())
