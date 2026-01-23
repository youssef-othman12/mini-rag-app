from helpers.config import get_settings ,settings
from fastapi import  UploadFile

class BaseController :
    
    def __init__(self):
        self.app_settings = get_settings()
    