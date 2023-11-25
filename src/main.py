from config import app_config

from fastapi import FastAPI
import uvicorn

from repository.service import AWSRepoService
from authentication.service import AuthService

app = FastAPI(description="Rest API Interface for the timer service")

from routes.media import MediaServiceHandler

# Initialize all app services
repo_service = AWSRepoService(storage_path=app_config.IMAGES_REPO_URL)
auth_service = AuthService(service_token_location=app_config.IDENTITY_TOKEN_LOCATION,
                           user_service_uri=app_config.AUTH_SERVICE_URL)


media_service = MediaServiceHandler(repo_service=repo_service, app_logging_service=None)
 
 #TODO: Bind auth service as middleware to all requests

# Connect all routes
app.include_router(media_service.router, prefix="/media")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", access_log=False)