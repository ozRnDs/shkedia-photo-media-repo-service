from config import app_config

from fastapi import FastAPI
import uvicorn

app = FastAPI(description="Rest API Interface for the timer service")

from routes.media import router
app.include_router(router, prefix="/media")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", access_log=False)