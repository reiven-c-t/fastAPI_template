from contextlib import contextmanager
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from db.base_class import Base
from db.session import SessionLocal
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    @contextmanager
    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read(self, db: Session, skip: int, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).filter(self.model.deleted_at == None).offset(skip).limit(limit).all()

    def read_one_by_id(self, db: Session, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.deleted_at == None, self.model.id == id).first()

    def read_one_by_value(self, db: Session, key: str, value: Any) -> Optional[ModelType]:  # TODO: test
        return (
            db.query(self.model)
            .filter(self.model.deleted_at == None, self.model.__getattribute__(key) == value)
            .first()
        )

    def read_one_by_values(self, db: Session, obj_in: Union[Dict[str, Any]]) -> ModelType:
        ...  # TODO

    def exist(self, db: Session, key: str, obj_in: Union[Dict[str, Any]]) -> bool:
        return self.read_one_by_values(db, obj_in=obj_in) is not None

    def update(self, db: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        obj.delete()
        db.add(obj)
        db.commit()
        return obj
