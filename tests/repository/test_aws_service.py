import pytest
from uuid import uuid4
from repository.service import AWSRepoService

@pytest.fixture(scope="module")
def basic_s3_object_fixture():
    fixture_s3 = AWSRepoService(storage_path="shekdia-dev-storage")

    yield fixture_s3

    fixture_s3.close()

@pytest.fixture(scope="module")
def object_key_fixture():
    return "test/"+str(uuid4())

@pytest.fixture(scope="module")
def object_content_fixture():
    return "Some test text"

def test_aws_upload(basic_s3_object_fixture: AWSRepoService, object_key_fixture: str, object_content_fixture: str):

    # Run
    basic_s3_object_fixture.upload(media_id=object_key_fixture, media_content=object_content_fixture.encode())


def test_aws_download_nominal(basic_s3_object_fixture: AWSRepoService, object_key_fixture, object_content_fixture:str):

    # Run
    downloaded_object: bytes = basic_s3_object_fixture.download(object_key_fixture)

    assert downloaded_object.decode() == object_content_fixture


def test_aws_delete_nominal(basic_s3_object_fixture: AWSRepoService, object_key_fixture):

    # Run
    delete_action_status = basic_s3_object_fixture.delete(media_id=object_key_fixture)

    # Assert
    assert delete_action_status == True


def test_aws_delete_error_media_not_exists(basic_s3_object_fixture: AWSRepoService):
    #TODO: We get false only for errors and not if media doesn't exist
    # Setup
    non_existance_object_key = "test/IdontExists"

    # Run
    delete_action_status = basic_s3_object_fixture.delete(media_id=non_existance_object_key)

    assert delete_action_status == False