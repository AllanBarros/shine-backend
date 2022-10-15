from fastapi import Depends
from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from models.event_model import Event

from configs.database_config import (
    get_db_connection,
)

class EventRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list_events(self) -> List[Event]:
        # name: Optional[str],
        # limit: Optional[int],
        # start: Optional[int],
            
        query = self.db.query(Event)

        # if name:
        #     query = query.filter_by(name=name)

        return query.all()

    def get_event_detail(self, value) -> Event:
        event = Event(id=value.id)
        result = self.db.get(Event, event.id, options=lazyload[Event.event_classifications])
        return result

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
        self.db.add(new_data)
        self.db.commit()
        self.db.refresh(new_data)
        return True
