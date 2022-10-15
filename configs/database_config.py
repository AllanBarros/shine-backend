
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from configs.env_config import EnvConfig

# Runtime Environment Configuration
env = EnvConfig()

# Generate Database URL
DATABASE_URL = env.db_uri

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, echo=False, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()