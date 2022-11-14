from typing import NamedTuple
from .infrastructor import Bucket, Rekognition

class ValidatorContainer(NamedTuple):
    bucket_service: Bucket
    rekognition_service: Rekognition

class BodyImage(NamedTuple):
    content: str
    name_image: str
    extension: str