from typing import List
from schemas.base_schema import BaseSchemaModel

class EventPostRequestSchema(BaseSchemaModel):
    event_name: str
    event_date: str
    event_country: str
    event_state: str
    event_city: str
    event_postal_code: str
    event_address: str
    event_complement: str
    event_description: str
    event_details: str
    event_tags: List[str]

class EventSchema(EventPostRequestSchema):
    id: int