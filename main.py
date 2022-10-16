from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.v1.classification_router import ClassficationRouter

from routers.v1.event_router import EventRouter
from models.base_model import init

init()

app = FastAPI()

origins = [
    "https://shine-frontend.azurewebsites.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(EventRouter)
app.include_router(ClassficationRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}

