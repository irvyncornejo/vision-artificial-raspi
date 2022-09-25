from typing import Any
import base64
import boto3
from .setting import BUCKET_NAME

class Bucket:
    def __init__(self):
        self._client: Any = boto3.client('s3')

    def create_object(self, content: str, name_image: str) -> None:
        file_content = base64.b64decode(content)

        try:
            self._client.put_object(
                Bucket=BUCKET_NAME,
                Key=f'image/{name_image}.png',
                Body=file_content
            )
        except Exception as e:
            print(e)

class Rekognition:
    def __init__(self):
        self._client: Any = boto3.client('rekognition')
        self._name_image: str = ''
    
    def _get_labels(self):
        response_label = self._client.detect_labels(
          Image={
              'S3Object':{
                'Bucket':BUCKET_NAME,
                'Name':f'image/{self._name_image}.png'
              }
          }
        )
        return response_label
    
    def _get_text(self):
        response_text = self._client.detect_text(
            Image={
              'S3Object':{
                'Bucket':BUCKET_NAME,
                'Name':f'image/{self._name_image}.png'
              }
          }
        )
        return response_text
    
    def validate(self, name_image: str):
        self._name_image = name_image
        print(self._get_text())
        print(self._get_labels())