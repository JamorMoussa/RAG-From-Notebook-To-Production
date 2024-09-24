from utils.config import Settings, get_settings
from controllers import DataController

from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

data_router = APIRouter(
    prefix= "/api/v1/data",
    tags= ["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str , file: UploadFile,
    app_settings: Settings = Depends(get_settings)
):
    is_valid, res_signal = DataController().validate_upload_file(file= file)

    if not is_valid:

        return JSONResponse(
            content= { 
                "signal": res_signal
            },
            status_code= status.HTTP_400_BAD_REQUEST
        )
    
    # TODO #3 Add logic to save file in assets/files folder 
    ## Video: mini-RAG | 07 | Uploading a File - 51:30 min
