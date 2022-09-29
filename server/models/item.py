from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text(1000))
    description = Column(Text(1000))
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
