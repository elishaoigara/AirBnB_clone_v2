# models/base_model.py
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dict_rep:
            del dict_rep["_sa_instance_state"]
        return dict_rep

    def save(self):
        """Saves the object to storage"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the object from storage"""
        models.storage.delete(self)

