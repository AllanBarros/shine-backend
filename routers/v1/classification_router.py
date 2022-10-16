from typing import List

from fastapi import APIRouter, Depends, status
from schemas.classification_schema import (
    ClassificationPostRequestSchema,
    ClassificationSchema,
    NewClassificationSchema,
)
from services.classification_service import ClassificationService

ClassficationRouter = APIRouter(prefix="/v1/tags", tags=["tags"])


@ClassficationRouter.get(
    "/listar", response_model=List[ClassificationPostRequestSchema]
)
def list(classificationService: ClassificationService = Depends()):
    return classificationService.list_tags()


@ClassficationRouter.post(
    "/adicionar",
    response_model=NewClassificationSchema,
    status_code=status.HTTP_201_CREATED,
)
def post_tag(tag: NewClassificationSchema,classificationService: ClassificationService = Depends()):
    return classificationService.add_tag(tag)
