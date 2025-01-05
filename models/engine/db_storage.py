# models/engine/db_storage.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database storage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            self.drop_all()

    def all(self, cls=None):
        """Returns all objects in storage"""
        if cls is None:
            query = self.__session.query(State, City, Amenity, User, Place, Review)
        else:
            query = self.__session.query(cls)

        all_objects = {}
        for obj in query.all():
            key = f"{obj.__class__.__name__}.{obj.id}"
            all_objects[key] = obj
        return all_objects

    def new(self, obj):
        """Adds the object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commits the session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database session and tables"""
        from models import Base
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

