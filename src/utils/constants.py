from vkwave.bots import Keyboard, ButtonColor
from skills.skills import content_plan_skill, create_article_skill
import messages
import config


MENU_KB = Keyboard(inline=True, one_time=True)
MENU_KB.add_text_button(
    text=content_plan_skill.button_name,
    payload={content_plan_skill.short_name: ""},
    color=ButtonColor.POSITIVE
)
MENU_KB.add_row()
MENU_KB.add_text_button(
    text=create_article_skill.button_name,
    payload={create_article_skill.short_name: ""},
    color=ButtonColor.POSITIVE
)


BACK_KB = Keyboard(inline=True, one_time=True)
BACK_KB.add_text_button(
    text=messages.BACK_BUTTON,
    payload={'command': 'menu'},
    color=ButtonColor.NEGATIVE
)

BACK_MENU_KB = Keyboard(inline=True, one_time=True)
BACK_MENU_KB.add_text_button(
    text=messages.MAIN_MENU_BUTTON,
    payload={'command': 'menu'},
    color=ButtonColor.NEGATIVE
)


VK_PAY_TEST_KEYBOARD = Keyboard(inline=True, one_time=True)
VK_PAY_TEST_KEYBOARD.add_vkpay_button_pay_to_group(
    1, config.VK_GROUP_ID, description="for cockies")
