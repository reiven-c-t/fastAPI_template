from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from utils.dt import dt


@as_declarative()
class Base:
    id: int = Column(Integer, primary_key=True, index=True)
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    created_at: datetime = Column(DateTime, default=dt.now())
    updated_at: datetime = Column(DateTime, default=dt.now(), onupdate=dt.now())
    deleted_at: datetime = Column(DateTime, nullable=True)

    def delete(self):
        self.deleted_at = dt.now()
