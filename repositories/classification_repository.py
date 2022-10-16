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

    def insert_tags(self, tag) -> Classification:
        new_tag = Classification()
        new_tag.classification_name = tag.classification_name
        new_tag.detail = tag.detail
        return new_tag

    def add_tag(self, new_data):
        new_tag = self.insert_tags(new_data)
        self.db.add(new_tag)
        self.db.commit()
        self.db.refresh(new_tag)
        return new_tag