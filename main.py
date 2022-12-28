from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import config
from da_vinchi import DaVinchi


bot = SimpleLongPollBot(tokens=config.VK_TOKEN, group_id=config.VK_GROUP_ID)
dv = DaVinchi(config.OPEN_AI_TOKEN)


@bot.message_handler()
async def echo(event: SimpleBotEvent) -> str:
	await event.answer('Ваш запрос находится в очереди, ожидайте...')
	answer = dv.send_question(event.object.object.message.text)
	await event.answer(answer)



print('start_bot')
bot.run_forever()
