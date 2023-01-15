import openai
import templates
import messages


class DaVinchi:
    def __init__(self, OPEN_AI_TOKEN):
        openai.api_key = OPEN_AI_TOKEN
        self.model_name = 'text-davinci-003'

    def get_content_plan_by_theme(self, theme: str) -> str:
        response = openai.Completion.create(
            model=self.model_name,
            prompt=templates.GET_CONTENT_PLAN_TEMPLATE.format(theme=theme),
            max_tokens=2000,
            temperature=0.3,
            top_p=1.0,
            frequency_penalty=0.1,
            presence_penalty=0.1,
            stop=['16.']
        )
        if len(response['choices']) == 0:
            return messages.BAD_RESULTAT_MESSAGE
        return response['choices'][0]['text']

    def get_atricle_by_theme(self, theme: str) -> str:
        response = openai.Completion.create(
            model=self.model_name,
            prompt=templates.GET_ARTICLE_BY_THEME_TEMPLATE.format(theme=theme),
            temperature=0.3,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        if len(response['choices']) == 0:
            return messages.BAD_RESULTAT_MESSAGE
        return response['choices'][0]['text']

    def send_question(self, question: str) -> str:
        response = openai.Completion.create(
            model=self.model_name,
            prompt=f"{question}",
            temperature=0.3,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        if len(response['choices']) == 0:
            return messages.BAD_RESULTAT_MESSAGE
        return response['choices'][0]['text']
