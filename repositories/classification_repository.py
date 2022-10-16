from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session
from models.classification_model import Classification

from configs.database_config import (
    get_db_connection,
)

class ClassificationRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list_tags(self) -> List[Classification]:
        query = self.db.query(Classification)
        return query.all()

    def get_tags_id(self, tags_list) -> List[Classification]:
        query = self.db.query(Classification)
        return query.filter(Classification.classification_name.in_(tags_list))
