import uvicorn
from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://034dc9bf20d9c847dfef935761fe8b76@o4506547783270400.ingest.sentry.io/4506554539048960",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI()


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
