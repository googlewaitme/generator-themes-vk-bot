import openai
import templates
import messages
import time

from openai import error
from sentry_sdk import capture_exception


def openai_errors(func):
    def _wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except error.ServiceUnavailableError:
            capture_exception(error.ServiceUnavailableError())
            return messages.SERVICE_IS_UNAVAILABLE
        except error.RateLimitError:
            capture_exception(error.RateLimitError())
            time.sleep(31)
            return _wrapper(*args, **kwargs)
        except Exception as e:
            capture_exception(e)
            return messages.UNEXCEPTED_ERROR
    return _wrapper


class DaVinchi:
    def __init__(self, OPEN_AI_TOKEN):
        openai.api_key = OPEN_AI_TOKEN
        self.model_name = 'text-davinci-003'

    @openai_errors
    def send_request(self, **kwargs):
        response = openai.Completion.create(**kwargs)
        if len(response['choices']) == 0:
            return messages.BAD_RESULTAT_MESSAGE
        return response['choices'][0]['text']

    @openai_errors
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
        params = {
            "max_tokens": 2048,
            "temperature": 0.3,
            "top_p": 0.8,
            "frequency_penalty": 0.1,
            "presence_penalty": 0.1
        }
        response = openai.Completion.create(
            model=self.model_name,
            prompt=f"{question}",
            **params
        )
        if len(response['choices']) == 0:
            return messages.BAD_RESULTAT_MESSAGE
        result = str(params) + response['choices'][0]['text']
        return result
