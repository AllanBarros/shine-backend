from fastapi import Depends
from typing import List
from sqlalchemy.orm import Session, lazyload
from models.event_model import Event
from configs.database_config import (
    get_db_connection,
)
from repositories.classification_repository import ClassificationRepository
from models.event_classification_model import event_classification

class EventRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list_events(self) -> List[Event]:    
        query = self.db.query(Event)
        result = query.all()
        return result

    def get_event_detail(self, value) -> Event:
        event = Event(id=value.id)
        result = self.db.get(Event, event.id, options=lazyload[Event.event_classifications])
        return result

    def event_classification_insert(self, event, tags):
        tags_id = ClassificationRepository.get_tags_id(self, tags.event_tags)
        for tag in tags_id:
            new_relation = event_classification.insert().values(
                event_id=event.id,
                classification_id=tag.id
            )
            self.db.execute(new_relation)
        self.db.commit()    
        return event
    
    def insert(self, values): 
        new_event = Event()
        new_event.event_name = values.event_name
        new_event.event_date = values.event_date
        new_event.event_country = values.event_country
        new_event.event_state = values.event_state
        new_event.event_city = values.event_city
        new_event.event_address = values.event_address
        new_event.event_postal_code = values.event_postal_code
        new_event.event_complement = values.event_complement
        new_event.event_description = values.event_description
        new_event.event_details = values.event_details
        return new_event

    def create(self, values) -> bool:
        new_data = self.insert(values)
        new_event = self.add_to_table(new_data)
        self.event_classification_insert(new_event, values)
        return True

    def add_to_table(self, new_data):
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return new_data