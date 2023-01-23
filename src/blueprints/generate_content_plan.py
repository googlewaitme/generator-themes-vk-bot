import json

from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    FiniteStateMachine,
    State,
    ForWhat,
    StateFilter,
    PayloadContainsFilter,
    Keyboard,
)

from skills.skills import content_plan_skill
import messages

new_content_plan_router = DefaultRouter()

fsm = FiniteStateMachine()


class SkillState:
    user_input = State("input")


@simple_bot_message_handler(
    new_content_plan_router,
    PayloadContainsFilter("create_content_plan"))
async def send_new_content_plan(event: SimpleBotEvent):
    payload = event.object.object.message.payload
    payload = json.loads(payload)
    theme = payload['create_content_plan']

    if len(theme) > 0:
        return await send_content_plan_by_theme(event, theme)

    await fsm.set_state(
        event=event, state=SkillState.user_input, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=content_plan_skill.request_for_skill_description,
        keyboard=Keyboard.get_empty_keyboard(),
    )


@simple_bot_message_handler(
    new_content_plan_router,
    StateFilter(
        fsm=fsm, state=SkillState.user_input, for_what=ForWhat.FOR_USER)
)
async def send_generated_article(event: SimpleBotEvent):
    theme = event.object.object.message.text
    if not theme:
        return await event.answer(message="Необходимо ввести текст")
    return await send_content_plan_by_theme(event, theme)


async def send_content_plan_by_theme(event: SimpleBotEvent, theme: str):
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    content_plan_skill.set_request(theme)
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=content_plan_skill.openai_answer,
        keyboard=content_plan_skill.keyboard)
