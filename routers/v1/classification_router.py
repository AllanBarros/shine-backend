from typing import List

from fastapi import APIRouter, Depends
from schemas.classification_schema import ClassificationPostRequestSchema
from services.classification_service import ClassificationService

ClassficationRouter = APIRouter(
    prefix="/v1/tags", tags=["tags"]
)

@ClassficationRouter.get("/listar", response_model=List[ClassificationPostRequestSchema])
def list(classificationService: ClassificationService = Depends()):
    return classificationService.list_tags()
