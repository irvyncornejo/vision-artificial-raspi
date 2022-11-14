import base64
from typing import Mapping, Any
from .domain import SchemaImage
from marshmallow.exceptions import ValidationError
from .services_types import ValidatorContainer, BodyImage

class IdentityValidator:
    def __init__(self, container: ValidatorContainer) -> None:
        self._image: BodyImage
        self._schema_image: Any = SchemaImage 
        self._bucket_service = container.bucket_service
        self._rekognition_service = container.rekognition_service
    
    def _decode_image(self) -> base64:
        return base64.b64decode(self._image['content'])

    def _validate_image(self, body: Mapping) -> None:
        self._error: Any = ''
        self._valid_schema: Any = True
        try:
            self._image = self._schema_image().load(body)
        
        except ValidationError as error:
            self._valid_schema = False
            self._error = error.normalized_messages()

    def _create_image(self):
        self._bucket_service.create_image(
            content=self._decode_image(),
            name_image=self._image['name_image'],
            extension=self._image['extension']
        )

    def _make_validation(self):
        self._rekognition_service.validate(
            content=self._decode_image()
        )

    def run(self, body: Mapping) -> Mapping:
        self._validate_image(body)
        if self._valid_schema:
            self._create_image()
            self._make_validation()
            return self._image
        return {'code': 400, 'errorMessage': self._error}

