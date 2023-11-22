from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

class MediaClass(BaseModel):
    media_name: str = None
    media_content: str = None


router = APIRouter(tags=["Media"])


@router.post("/")
def post_media(media: UploadFile(...)):
    media_name = media.file.filename()
    return "test"

@router.get("/{media_id}",
            response_model=str,
            summary="Get media by id",
            description="Get media from repo by id")
def get_media(media_id: str):
    return "This is media"

