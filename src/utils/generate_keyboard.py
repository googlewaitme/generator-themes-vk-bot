from vkwave.bots import Keyboard, ButtonColor
import messages


def get_key_for_skills(button_again_name: str, payload):
    key = Keyboard(inline=True)
    key.add_text_button(
        text=messages.MAIN_MENU_BUTTON,
        payload={"command": "menu"},
        color=ButtonColor.POSITIVE
    )
    key.add_text_button(
        text=button_again_name,
        payload=payload,
        color=ButtonColor.POSITIVE
    )
    return key
