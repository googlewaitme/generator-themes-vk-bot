from environs import Env

env = Env()
env.read_env()

VK_TOKEN = env.str('VK_TOKEN')
VK_GROUP_ID = env.str('VK_GROUP_ID')
VK_GROUP_NAME = env.str('VK_GROUP_NAME', "public" + VK_GROUP_ID)
OPEN_AI_TOKEN = env.str('OPEN_AI_TOKEN')

# --- Sentry SDK ---

SENTRY_SDK_RUN = env.bool("SENTRY_SDK_RUN", False)
if SENTRY_SDK_RUN:
    SENTRY_SDK_TOKEN = env.str("SENTRY_SDK_TOKEN")

# --- DATABASE ---

DATABASE_NAME = env.str("DATABASE_NAME", "users.db")

# --- REDIS ---

REDIS_HOST = env.str("REDIS_HOST", "localhost")
REDIS_PORT = env.int("REDIS_PORT", 6379)

# --- SPAM CONTROL ---

LIMIT_NUMBER_OF_MESSAGES_PER_HOUR = env.int(
    "LIMIT_NUMBER_OF_MESSAGES_PER_HOUR", 90)
