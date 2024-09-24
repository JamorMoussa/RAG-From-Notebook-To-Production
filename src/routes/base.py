from utils.config import Settings, get_settings

from fastapi import APIRouter, Depends


base_router = APIRouter(
    prefix= "/api/v1",
    tags= ["api_v1", ]
)


@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):

    app_name = app_settings.APP_NAME 
    app_version = app_settings.APP_VERSION
    
    return {
        "app name": app_name,
        "app version": app_version 
    }