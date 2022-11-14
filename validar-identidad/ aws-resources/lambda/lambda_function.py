from services import IdentityValidator
from services import Bucket
from services import Rekognition
from services.services_types import ValidatorContainer

def get_validator_container() -> ValidatorContainer:
    return ValidatorContainer(
        bucket_service=Bucket(),
        rekognition_service=Rekognition()
    )

def lambda_handler(event, context: None):
    return IdentityValidator(
        container=get_validator_container()
    ).run(event)


lambda_handler({
    'name_image': 'nombre_test',
    'extension': 'png',
    'content': ""
}, {})