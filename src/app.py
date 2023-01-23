import logging

from vkwave.bots import SimpleLongPollBot

import redis

from da_vinchi import DaVinchi
import config
from middlewares.user_data_middleware import UserMiddleware
from middlewares.spam_control import SpamControlMiddleware
from middlewares.referal_system_middleware import ReferalSystemMiddleware
from middlewares.set_user_id_middleware import SetUserIDMiddleware

from blueprints import (menu_router,
                        back_router,
                        sandbox_router,
                        referal_system_router,
                        new_article_router,
                        new_content_plan_router,
                        vk_pay_router)


logging.basicConfig(level=logging.INFO)

bot = SimpleLongPollBot(tokens=config.VK_TOKEN, group_id=config.VK_GROUP_ID)
dv = DaVinchi(config.OPEN_AI_TOKEN)

spam_controller = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=1
)


bot.middleware_manager.add_middleware(SetUserIDMiddleware())

bot.middleware_manager.add_middleware(SpamControlMiddleware(spam_controller))
bot.middleware_manager.add_middleware(UserMiddleware())
bot.middleware_manager.add_middleware(ReferalSystemMiddleware())


bot.dispatcher.add_router(back_router)

bot.dispatcher.add_router(vk_pay_router)

bot.dispatcher.add_router(sandbox_router)
bot.dispatcher.add_router(referal_system_router)

bot.dispatcher.add_router(new_article_router)
bot.dispatcher.add_router(new_content_plan_router)

bot.dispatcher.add_router(menu_router)

logging.info('start_bot')

bot.run_forever()
