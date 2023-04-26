#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property def cities(self):
        values_city = models.storage.all()
        list_city = []
        result = []
        for key in values_city:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_city.append(values_city[key])
        for elem in list_city:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
