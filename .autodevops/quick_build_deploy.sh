cz bump -ch

export MEDIA_REPO_SERVICE_VERSION=$(cz version -p)
export IMAGE_NAME=shkedia-photo-media-repo-service:${MEDIA_REPO_SERVICE_VERSION}
export IMAGE_FULL_NAME=public.ecr.aws/q2n5r5e8/ozrnds/${IMAGE_NAME}

docker build . -t ${IMAGE_FULL_NAME}

export ENVIRONMENT=dev
export ENV_FILE=.local/media_repo_service_${ENVIRONMENT}.env
docker compose --env-file ${ENV_FILE} up -d