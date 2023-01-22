from da_vinchi import DaVinchi
import config
import sentry_sdk


dv = DaVinchi(config.OPEN_AI_TOKEN)

if config.SENTRY_SDK_RUN:
    sentry_sdk.init(
        dsn=config.SENTRY_SDK_TOKEN,
        traces_sample_rate=1.0
    )
