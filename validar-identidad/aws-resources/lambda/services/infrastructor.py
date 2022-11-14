from typing import Any
import base64
import boto3
from .setting import BUCKET_NAME

class Bucket:
    def __init__(self):
        self._client: Any = boto3.client('s3')

    def create_image(self, content: base64, name_image: str, extension: str) -> None:
        try:
            self._client.put_object(
                Bucket=BUCKET_NAME,
                Key=f'image/{name_image}.{extension}',
                Body=content
            )
        except Exception as e:
            print(e)

class Rekognition:
    def __init__(self):
        self._client: Any = boto3.client('rekognition')
        self._content: str = ''

    def _get_text(self):
        response_text = self._client.detect_text(
            Image={
              "Bytes": self._content
          }
        )
        return response_text
    
    def validate(self, content: base64):
        self._content = content
        print(self._get_text())