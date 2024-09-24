from enum import Enum


class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS: str = "File validated success"
    FILE_TYPE_NOT_SUPPORTED: str = "File type is not supported"
    FILE_SIZE_EXCEEDED: str = "File size exceeded"
    FILE_UPLOAD_SUCCESS: str = "File upload success"
    FILE_UPLOAD_FAILED: str = "File upload failed"