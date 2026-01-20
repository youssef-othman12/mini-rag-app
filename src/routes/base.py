from fastapi import FastAPI , APIRouter , Depends
from helpers.config import get_settings ,settings
import os 
base_router = APIRouter(
    prefix="/api/v1",
    tags =["api_v1"]
)
@base_router.get("/")
async def welcome(app_settings : settings = Depends(get_settings)):
    
    app_name = app_setting.APP_NAME
    app_version = app_setting.APP_VERSION
    return{
       "APP_NAME" : app_name,
       "APP_VERSION" : app_version,
    }