from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, Text
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(Text, index=False)
    email = Column(Text(256), unique=True, index=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
