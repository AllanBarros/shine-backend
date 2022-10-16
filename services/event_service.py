from fastapi import Depends
from repositories.event_repository import EventRepository

class EventService:
    
    eventRepository:EventRepository

    def __init__(
        self, eventRepository: EventRepository = Depends()
    ) -> None:
        self.eventRepository = eventRepository

    def list_events(self):
        results = self.eventRepository.list_events()
        return results

    def get_event_detail(self, event):
        return self.eventRepository.get_event_detail(event)
    
    def create_event(self, event):
        self.event = event
        return self.eventRepository.create(event)
