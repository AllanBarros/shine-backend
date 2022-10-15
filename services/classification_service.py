from fastapi import Depends
from repositories.classification_repository import ClassificationRepository


class ClassificationService:
    
    classificationRepository: ClassificationRepository

    def __init__(
        self, classificationRepository: ClassificationRepository = Depends()
    ) -> None:
        self.classificationRepository = classificationRepository

    def list_tags(self):
        return self.classificationRepository.list_tags()
