#!/usr/bin/python3
""" DBStorage engine for AirBnB clone """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import models

class DBStorage:
    """DBStorage engine for interacting with the database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')

        # Create engine
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True
        )

        # Drop tables if environment is test
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects from the database"""
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for clss in models.classes.values():
                objects += self.__session.query(clss).all()
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}

    def new(self, obj):
        """Add new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit session changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

