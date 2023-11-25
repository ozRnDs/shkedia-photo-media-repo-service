# shkedia-photo-media-repo-service

# Overview
The Media Repo service for the Shkedia Private Images Cloud system. 
It will handle the communication between the entire system and the chosen storage that will handle the crypted images.
This will be CRUD RESTful API based on FastAPI.

## The service actions
GET /media/{media_id}  
POST /media  
DELETE /media/{media_id}

# Deploy
## AWS Credentials
In case the container is on AWS machine, make sure that machine has built in credentials to s3 bucket.  
In order to work with aws repository, with a machine outside the AWS cloud, there should be 2 files maped to the container as follow:
```bash
cat << EOT >> ~/.aws/config
    [default]
    region = <the region of the bucket>
    EOT

cat << EOT >> ~/.aws
    [default]
    aws_access_key_id = <The application's account access key>
    aws_secret_access_key = <The application's account secret access key>
    EOT
```

## Manual Deployment
1. Set the image version and needed parameters:
    ```bash
    # Container Settings
    export IMAGE_VERSION=0.0.1
    export IMAGE_NAME=shkedia-photo-media-repo-service:${IMAGE_VERSION}
    export SERVICE_PORT=5555
    export CONTAINER_NAME=shkedia-media-repo-service
    export AWS_CREDENTIALS_LOCATION=<WRITE THE AWS CREDENTIALS LOCATION>

    # Application Configuration Variables
    export IMAGE_REPO_URL=shekdia-dev-storage
    ```
2. Run the docker
    ```bash
    docker run -d --restart=always -p ${SERVICE_PORT}:5000 \
    -v ${AWS_CREDENTIALS_LOCATION}:/root/.aws \
    -e IMAGES_REPO_URL=${IMAGE_REPO_URL} \
    --name ${CONTAINER_NAME} ${IMAGE_NAME}
    ```
    
# Development
## Environment
The best environment for developing the component is using .vscode with devcontainer.  
User *ctrl+shift+p* and write *Recreate container* to open the development folder with all the dependencies of the application.

The container is based on python 3.11.6
## Build
1. Bump the version of the project using commitizen
```bash
cz bump
```
2. Create the image with the current version
```bash
export IMAGE_VERSION=$(cz version --project)
docker build . -t shkedia-media-repo-service:${IMAGE_VERSION}
```
## Test


