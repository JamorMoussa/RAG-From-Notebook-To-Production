from fastapi import APIRouter
import os 

base_router = APIRouter(
    prefix= "/api/v1",
    tags= ["api_v1", ]
)


@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    
    return {
        "app name": app_name,
        "app version": app_version 
    }