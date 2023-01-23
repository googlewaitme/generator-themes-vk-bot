from vkwave.bots import Keyboard, ButtonColor
import messages
import config


MENU_KB = Keyboard(inline=True)
MENU_KB.add_text_button(
    text=messages.CREATE_CONTENT_PLAN_BUTTON,
    payload={"create_content_plan": ""},
    color=ButtonColor.POSITIVE
)
MENU_KB.add_row()
MENU_KB.add_text_button(
    text=messages.CREATE_ARTICLE_BUTTON,
    payload={"command": "create_article"},
    color=ButtonColor.POSITIVE
)


BACK_KB = Keyboard(inline=True)
BACK_KB.add_text_button(
    text=messages.BACK_BUTTON,
    payload={'command': 'menu'},
    color=ButtonColor.NEGATIVE
)

BACK_MENU_KB = Keyboard(inline=True)
BACK_MENU_KB.add_text_button(
    text=messages.MAIN_MENU_BUTTON,
    payload={'command': 'menu'},
    color=ButtonColor.NEGATIVE
)


VK_PAY_TEST_KEYBOARD = Keyboard(inline=True)
VK_PAY_TEST_KEYBOARD.add_vkpay_button_pay_to_group(
    1, config.VK_GROUP_ID, description="for cockies")
