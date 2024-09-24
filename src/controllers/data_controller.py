from .base import BaseController
from models import ResponseSignal

from fastapi import UploadFile

class DataController(BaseController):
    
    def __init__(self):
        super(DataController, self).__init__()

        self.size_scale: int = 1048576 # MB to bytes

    def validate_upload_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value