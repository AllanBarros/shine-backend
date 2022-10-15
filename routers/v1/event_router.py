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

@EventRouter.get("/listar", response_model=List[EventSchema])
def list(eventService: EventService = Depends()):
    return eventService.list_events()

@EventRouter.post(
    "/criar",
    response_model=EventPostRequestSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    event: EventPostRequestSchema,
    eventService: EventService = Depends(),
):
    return eventService.create_event(event)


# @EventRouter.patch("/{id}", response_model=AuthorSchema)
# def update(
#     id: int,
#     author: AuthorPostRequestSchema,
#     authorService: AuthorService = Depends(),
# ):
#     return authorService.update(id, author).normalize()


# @EventRouter.delete(
#     "/{id}", status_code=status.HTTP_204_NO_CONTENT
# )
# def delete(
#     id: int, authorService: AuthorService = Depends()
# ):
#     return authorService.delete(id)


# @EventRouter.get(
#     "/{id}/books/", response_model=List[BookSchema]
# )
# def get_books(
#     id: int, authorService: AuthorService = Depends()
# ):
#     return [
#         book.normalize()
#         for book in authorService.get_books(id)
#     ]