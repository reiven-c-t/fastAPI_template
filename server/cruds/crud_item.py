from typing import List

from cruds.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.item import Item
from schemas.item import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(self, db: Session, *, obj_in: ItemCreate, owner_id: int) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read_multi_by_owner(self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        return (
            db.query(self.model)
            .filter(self.model.deleted_at == None, Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


item = CRUDItem(Item)
