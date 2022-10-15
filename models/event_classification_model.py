from sqlalchemy import Column, ForeignKey, Table

from models.base_model import Base

event_classification = Table(
    "event_classification",
    Base.metadata,
    Column("event_id", ForeignKey("events.id")),
    Column("classification_id", ForeignKey("classifications.id")),
)
