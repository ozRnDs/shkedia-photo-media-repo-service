## 0.2.0 (2023-12-01)

### Feat

- **routes/media/put_image**: Change route method to PUT. Get blob name from the file in the request. Upload the file in a dated folder. Return MediaStoreInfo object as response

## 0.1.0 (2023-11-25)

### Feat

- **main,config**: Bind the services to the FastAPI application. Add important configuration variables to the config file
- **src/routes/media**: Create routes for uploading, downloading and deleting media from a reposervice
- **src/repository**: Create aws repository service to be used in the routes
- **project-init**: Create the basic fastapi project structure

### Refactor

- **src/authentication**: Create basic template for the authentication service
