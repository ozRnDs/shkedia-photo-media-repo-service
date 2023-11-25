import logging
import boto3
logger = logging.getLogger(__name__)

from unittest.mock import MagicMock


class RepoService:
    def __init__(self):
        #TODO: Add repository connections parameters (Host,Port,User,Password)
        self.repo_object = MagicMock()
        pass

    def upload(self,media_id: str, media_content: bytes) -> None:
        logger.info(f"Uploaded {media_id}")
        return
    
    def is_ready(self) -> bool:
        # TODO: Create the correct logic depending on the repo service
        if self.repo_object is None:
            return False
        return True
    
    def download(self, media_id: str) -> bytes:
        media_content = None
        if media_id == "test":
            media_content = "Testing Response"
        if media_content is None:
            raise FileNotFoundError("Can't find media")
        return media_content.encode()
    
    def delete(self, media_id: str) -> bool:
        self.repo_object.delete_blob_method(media_id)
        return media_id
    
    def close(self):
        self.repo_object.close()
    
class AWSRepoService(RepoService):
    def __init__(self, 
                    storage_path: str):
        self.storage_path = storage_path
        self.repo_object = boto3.client('s3')

    def upload(self, media_id: str, media_content: bytes) -> None:
        upload_response = self.repo_object.put_object(Bucket=self.storage_path,
                                    Key=media_id,
                                    Body=media_content,
                                    )
        if not "ETag" in upload_response:
            raise Exception("Unexpected response from AWS server")

    def delete(self, media_id: str) -> bool:
        try:
            self.repo_object.delete_object(Bucket=self.storage_path,
                                        Key=media_id)
            return True
        except Exception as err:
            logger.error(str(err))
            return False

    def download(self, media_id: str) -> bytes:
        try:
            download_response = self.repo_object.get_object(Bucket=self.storage_path,
                                                            Key=media_id)
            if "Body" in download_response:
                body = download_response["Body"].read()
                return body

        except Exception as err:
            logger.error(str(err))