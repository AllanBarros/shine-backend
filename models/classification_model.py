from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.event_classification_model import event_classification

class Classification(Base):
    __tablename__ = "classifications"

    id=Column(Integer)
    classification_name=Column(String(50), nullable=False)
    detail=Column(String(50), nullable=False)
    tag_events=relationship(
        "Event",
        lazy="dynamic",
        secondary=event_classification,
    )

    PrimaryKeyConstraint(id)
