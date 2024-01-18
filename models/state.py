#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship(
        "City", backref='state', cascade="all, delete, delete-orphan")

    # For FileStorage
    def cities(self):
        return [city for city in self.cities
                if city.state_id == self.id]
