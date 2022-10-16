from typing import List

from fastapi import APIRouter, Depends, status

from schemas.event_schema import EventPostRequestSchema, EventSchema
from services.event_service import EventService

EventRouter = APIRouter(
    prefix="/v1/eventos", tags=["eventos"]
)

# @EventRouter.get("/detalhes", response_model=List[EventSchema])
# def index(
#     name: Optional[str] = None,
#     pageSize: Optional[int] = 100,
#     startIndex: Optional[int] = 0,
#     authorService: AuthorService = Depends(),
# ):
#     return [
#         author.normalize()
#         for author in authorService.list(
#             name, pageSize, startIndex
#         )
#     ]


@EventRouter.get("/detalhes/{id}", response_model=EventSchema)
def get(id: int, eventService: EventService = Depends()):
    return eventService.get_event_detail(id)

@EventRouter.get("/listar", response_model=List)
def list(eventService: EventService = Depends()):
    return eventService.list_events()

@EventRouter.post(
    "/criar",
    status_code=status.HTTP_201_CREATED,
)
def create(
    event: EventPostRequestSchema,
    eventService: EventService = Depends(),
):
    return eventService.create_event(event)
