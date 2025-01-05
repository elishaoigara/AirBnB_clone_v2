#!/usr/bin/python3
""" BaseModel class for AirBnB clone in SQLAlchemy """

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """Base class for all models in the AirBnB clone"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Save the current instance to storage"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance to dictionary"""
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dict_obj:
            del dict_obj["_sa_instance_state"]
        return dict_obj

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
