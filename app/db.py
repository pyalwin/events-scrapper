# app/db.py

import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Events(ormar.Model):
    class Meta(BaseMeta):
        tablename = "events"

    id: int = ormar.Integer(primary_key=True)
    event_date: str = ormar.Date(nullable=True)
    event_time: str = ormar.Time(nullable=True)
    event_title: str = ormar.String(max_length=255, unique=True, nullable=False)
    event_subtitle: str = ormar.String(max_length=255, nullable=True)
    event_location: str = ormar.String(max_length=255, nullable=True)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)