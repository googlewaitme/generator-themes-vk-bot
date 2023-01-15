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
    CommandsFilter,
    Keyboard,
)

from utils.generate_keyboard import get_key_for_skills
from loader import dv
import messages

sandbox_router = DefaultRouter()

fsm = FiniteStateMachine()


class SandboxState:
    user_input = State("input")


@simple_bot_message_handler(
    sandbox_router,
    CommandsFilter("start_sandbox"))
async def start_sandbox(event: SimpleBotEvent):
    await fsm.set_state(
        event=event, state=SandboxState.user_input, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=messages.SANDBOX_HELLO_MESSAGE,
        keyboard=Keyboard.get_empty_keyboard(),
    )


@simple_bot_message_handler(
    sandbox_router,
    StateFilter(
        fsm=fsm,
        state=SandboxState.user_input,
        for_what=ForWhat.FOR_USER)
)
async def send_generated_article(event: SimpleBotEvent):
    theme = event.object.object.message.text
    if not theme:
        return await event.answer(message="Необходимо ввести текст")
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    answer = dv.send_question(theme)
    generated_keyboard = get_key_for_skills(
        button_again_name=messages.NEW_ARTICLE_BACK_BUTTON,
        payload={"new_request_sandbox": theme})
    return await event.answer(
        answer,
        keyboard=generated_keyboard.get_keyboard())


@simple_bot_message_handler(
    sandbox_router,
    PayloadContainsFilter("new_request_sandbox"))
async def new_generation_content_plan_by_old_theme(event: SimpleBotEvent):
    payload = event.object.object.message.payload
    payload = json.loads(payload)
    theme = payload['new_request_sandbox']
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    answer = dv.send_question(theme)
    generated_keyboard = get_key_for_skills(
        button_again_name=messages.NEW_ARTICLE_BACK_BUTTON,
        payload={"new_request_sandbox": theme})
    # await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        answer,
        keyboard=generated_keyboard.get_keyboard())
