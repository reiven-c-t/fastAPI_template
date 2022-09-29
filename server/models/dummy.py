from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Column, Integer, Text

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Dummy(Base):
    id = Column(Integer, primary_key=True, index=True)
    menu = Column(Text(1000))
    description = Column(Text(1000))
    count = Column(Integer, default=0)
