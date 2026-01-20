from fastapi import FastAPI , APIRouter , Depends
from helpers.config import get_settings ,settings
import os 
data_router = APIRouter(
    prefix="/api/v1/data",
    tags =["api_v1","data"]
)
@data_router.post("/upload")