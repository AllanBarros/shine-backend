from schemas.base_schema import BaseSchemaModel

class ClassificationPostRequestSchema(BaseSchemaModel):
    classification_name: str
    
class ClassificationSchema(ClassificationPostRequestSchema):
    id: int

class NewClassificationSchema(ClassificationPostRequestSchema):
    detail: str
