import openai
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
