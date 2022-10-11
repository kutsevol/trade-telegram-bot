import sentry_sdk
from envs import env_vars

sentry_sdk.init(
    dsn=env_vars.sentry_dsn,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
