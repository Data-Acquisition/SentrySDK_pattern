import sentry_sdk

sentry_sdk.init(
    dsn="https://a71ee30a7752581ae8394cd12b864771@o4506547783270400.ingest.sentry.io/4506548282327040",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    environment="dev",
)
