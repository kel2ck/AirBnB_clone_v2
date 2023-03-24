#!/usr/bin/python3
"""Implementation of DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


classes = {"State": State, "City": City}
class DBStorage:
    """Implementation of the database storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")
        environment = os.environ.get("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, password, database),
                                      pool_pre_ping=True)
        if environment == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Prints all the objects of a class, if the class is provided.
        If not, prints all objects
        """
        object_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
            for object in objects:
                key = object.__class__.__name__ + '.' + object.id
                object_dicts[key] = object
        else:
            for item in classes.values():
                objects = self.__session.query(item).all()
                for object in objects:
                    key = object.__class__.__name__ + '.' + object.id
                    object_dicts[key] = object
        return object_dict

    def new(self, obj):
        """adds the object to the session"""
        self.__session.add(obj)

    def save(self):
        """commits the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the object from the session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """loads and creates the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
