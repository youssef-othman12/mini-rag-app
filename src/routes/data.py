from fastapi import FastAPI , APIRouter , Depends ,UploadFile
from helpers.config import get_settings ,settings
import os 
from controllers import DataController
data_router = APIRouter(
    prefix="/api/v1/data",
    tags =["api_v1","data"],
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str ,file : UploadFile,
                      app_settings : settings = Depends(get_settings)):
      is_valid , result_signal = DataController().Validate_upload_file(file=file)
      return {
              "singnal": result_signal}