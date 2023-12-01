from fastapi import APIRouter, HTTPException, UploadFile, Depends, Body
from fastapi.responses import Response
from pydantic import BaseModel
from uuid import uuid4

from repository.service import AWSRepoService, MediaStorageInfo

class MediaClass(BaseModel):
    media_id: str = str(uuid4())
    media_content: bytes = None

class SuccessResponse(BaseModel):
    media_id: str = str(uuid4())

router = APIRouter(tags=["Media"])


class MediaServiceHandler:
    def __init__(self, 
                 repo_service: AWSRepoService,
                 app_logging_service
                 ):
        self.repo_service = repo_service
        self.logging_service = app_logging_service
        if not self.repo_service.is_ready():
            raise Exception("Can't initializes without repo_service")
        self.router = self.__initialize_routes__()


    def __initialize_routes__(self):
        router = APIRouter(tags=["media"])
        router.add_api_route(path="/", 
                             endpoint=self.put_media,
                             methods=["put"],
                             response_model=MediaStorageInfo)
        router.add_api_route(path="/{service_name}/{bucket_name}/{media_id}", 
                             endpoint=self.get_media,
                             methods=["get"])
        router.add_api_route(path="/{service_name}/{bucket_name}/{media_id}", endpoint=self.delete_media, methods=["delete"])
        return router


    def put_media(self, media: UploadFile) -> MediaStorageInfo:
        media_id = media.filename
        temp_media_object = MediaClass(media_id=media_id, media_content=media.file.read())
        try:
            media_storage_info = self.repo_service.upload(media_id=temp_media_object.media_id,
                                     media_content=temp_media_object.media_content)
            return media_storage_info
        except Exception as err:
            #TODO: Log the full err
            raise HTTPException(status_code=500,detail="Could not upload the image")

    def get_media(self, media_id: str):
        try:
            media_byte = self.repo_service.download(media_id=media_id)
            return Response(content=media_byte, media_type="application/octet-stream")
        except FileNotFoundError as err:
            #TODO: Log the full err
            raise HTTPException(status_code=404,detail="Could not find media")
        except Exception as err:
            #TODO: Log the full err
            raise HTTPException(status_code=500,detail="Can't reach images storage")

    def delete_media(self, media_id: str):
        try:
            if self.repo_service.delete(media_id=media_id):
                return SuccessResponse(media_id=media_id)
            raise HTTPException("Media wasn't deleted")
        except Exception as err:
            #TODO: Log the full err
            raise HTTPException("Can't delete the media")