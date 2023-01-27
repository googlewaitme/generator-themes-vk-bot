from utils.generate_keyboard import get_key_for_skills
from loader import dv


class Skill:
    def __init__(
            self,
            short_name: str,
            verbose_name: str,
            name: str,
            request_for_skill_description: str,
            openai_data: dict,
            prompt_template: str,
            button_name: str,
            restart_button_name: str,
            max_len_request: int = 100):
        self.short_name = short_name
        self.verbose_name = verbose_name
        self.name = name

        self.request_for_skill_description = request_for_skill_description

        self.openai_data = openai_data

        self.button_name = button_name
        self.restart_button_name = restart_button_name
        self.prompt_template = prompt_template

        self.max_len_request = max_len_request

    def set_request(self, request: str):
        self.send_request_openai(request)
        self.generate_keyboard(request)

    def send_request_openai(self, req: str):
        self.openai_data['prompt'] = self.prompt_template.format(request=req)
        self.openai_answer = dv.send_request(**self.openai_data)

    def generate_keyboard(self, request: str):
        keyboard = get_key_for_skills(
            self.restart_button_name, payload={self.short_name: request})
        self.keyboard = keyboard.get_keyboard()
