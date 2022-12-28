import openai


class DaVinchi:
	def __init__(self, OPEN_AI_TOKEN):
		openai.api_key = OPEN_AI_TOKEN

	def send_question(self, question):
		response = openai.Completion.create(
			model="text-davinci-003",
			prompt=f"{question}",
			temperature=0.3,
			max_tokens=3000,
			top_p=1.0,
			frequency_penalty=0.0,
			presence_penalty=0.0
		)
		return response['choices'][0]['text']
