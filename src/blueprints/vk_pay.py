from vkwave.bots import (
    DefaultRouter,
    SimpleBotEvent,
    simple_bot_message_handler,
    simple_bot_handler,
    CommandsFilter,
    FiniteStateMachine,
)

from vkwave.bots.core.dispatching import filters
import messages
from utils.constants import VK_PAY_TEST_KEYBOARD

vk_pay_router = DefaultRouter()

fsm = FiniteStateMachine()


@simple_bot_message_handler(
    vk_pay_router, filters.EventTypeFilter("vkpay_transaction"))
async def send_about_getted_sum(event: SimpleBotEvent):
    # TODO me
    return await event.answer(message='getted sum money')


@simple_bot_message_handler(vk_pay_router, CommandsFilter('test_vk_pay'))
async def send_test_vk_pay_keyboard(event: SimpleBotEvent):
    return await event.answer(
        message=messages.GETTING_THEME_TO_ARTICLE,
        keyboard=VK_PAY_TEST_KEYBOARD.get_keyboard(),
    )
