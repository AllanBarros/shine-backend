from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from models.base_model import Base
from models.event_classification_model import event_classification


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer)
    event_name = Column(String(255), nullable=False)
    event_date = Column(String(8), nullable=False)
    event_country = Column(String(25), nullable=False)
    event_state = Column(String(30), nullable=False)
    event_city = Column(String(40), nullable=False)
    event_postal_code = Column(String(10), nullable=False)
    event_address = Column(String(255), nullable=False)
    event_complement = Column(String(255), nullable=False)
    event_description = Column(String(255), nullable=False)
    event_details = Column(String(255), nullable=False)
    event_tags = relationship(
        "Classification",
        lazy="joined",
        secondary=event_classification,
    )

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "event_name": self.event_name.__str__(),
            "event_date": self.event_date.__str__(),
            "event_country": self.event_country.__str__(),
            "event_state": self.event_state.__str__(),
            "event_city": self.event_city.__str__(),
            "event_postal_code": self.event_postal_code.__str__(),
            "event_address": self.event_address.__str__(),
            "event_complement": self.event_complement.__str__(),
            "event_description": self.event_description.__str__(),
            "event_details":self.event_details.__str__(),
            "event_tags": self.event_tags.__str__(),
        }