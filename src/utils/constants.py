from vkwave.bots import Keyboard, ButtonColor
import messages


MENU_KB = Keyboard(inline=True)
MENU_KB.add_text_button(
    text=messages.CREATE_CONTENT_PLAN_BUTTON,
    payload={"command": "create_content_plan"},
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
