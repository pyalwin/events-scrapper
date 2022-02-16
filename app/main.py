from fastapi import FastAPI
from .db import database, Events

from pydantic import BaseModel

from .utils import ParseSite

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to api"}

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

class SiteParams(BaseModel):
    url: str

@app.post('/fetch-events')
async def parse_site(params: SiteParams):
    event_data = ParseSite(params.url).process()
    for event in event_data:
        try:
            await Events.objects.create(**event)
        except Exception as e:
            print(e)
    return {"message": f"{len(event_data)} events loaded into database successfully"}

@app.get('/events')
async def get_events():
    return await Events.objects.all()

@app.get('/flush-events')
async def flush_events():
    return await Events.objects.delete(each=True)
