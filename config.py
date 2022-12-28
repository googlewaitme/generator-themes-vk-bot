from environs import Env

env = Env()
env.read_env()

VK_TOKEN = env.str('VK_TOKEN')
VK_GROUP_ID = env.str('VK_GROUP_ID')
OPEN_AI_TOKEN = env.str('OPEN_AI_TOKEN')
