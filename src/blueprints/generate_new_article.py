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

from vkwave.bots.core.dispatching.filters import builtin

from skills.skills import create_article_skill

import messages

new_article_router = DefaultRouter()

fsm = FiniteStateMachine()


class SkillState:
    user_input = State("input")


@simple_bot_message_handler(
    new_article_router,
    PayloadContainsFilter(create_article_skill.short_name))
async def send_new_content_plan(event: SimpleBotEvent):
    payload = event.object.object.message.payload
    payload = json.loads(payload)
    theme = payload[create_article_skill.short_name]

    if len(theme) > 0:
        return await send_content_plan_by_theme(event, theme)

    await fsm.set_state(
        event=event, state=SkillState.user_input, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=create_article_skill.request_for_skill_description,
        keyboard=Keyboard.get_empty_keyboard(),
    )


@simple_bot_message_handler(
    new_article_router,
    StateFilter(
        fsm=fsm, state=SkillState.user_input, for_what=ForWhat.FOR_USER),
    lambda event: builtin.get_payload(event) is None
)
async def send_generated_article(event: SimpleBotEvent):
    theme = event.object.object.message.text
    if not theme:
        return await event.answer(message="Необходимо ввести текст")
    if len(theme) > create_article_skill.max_len_request:
        return await event.answer(
            message="Слишком длинный запрос для данного навыка")
    return await send_content_plan_by_theme(event, theme)


@simple_bot_message_handler(
    new_article_router,
    StateFilter(
        fsm=fsm, state=SkillState.user_input, for_what=ForWhat.FOR_USER))
async def send_error_message_about_buttons(event: SimpleBotEvent):
    return await event.answer(
        message=create_article_skill.request_for_skill_description,
        keyboard=Keyboard.get_empty_keyboard(),
    )


async def send_content_plan_by_theme(event: SimpleBotEvent, theme: str):
    await event.answer(messages.WAITING_RESULT_MESSAGE)
    create_article_skill.set_request(theme)
    if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
        await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
    return await event.answer(
        message=create_article_skill.openai_answer,
        keyboard=create_article_skill.keyboard)
