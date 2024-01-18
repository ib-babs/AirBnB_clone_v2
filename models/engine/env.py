#!/usr/bin/python3
from sqlalchemy import Column, String, DATETIME
from datetime import datetime
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column, ForeignKey
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()


"""This module defines a base class for all models in our hbnb clone"""
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state') is not None:
            dictionary.__delitem__('_sa_instance_state')
        return dictionary

    def delete(self):
        """Deletes current instance from the storage"""
        from models import storage
        storage.delete(self)


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship(
        "City", backref='state', cascade="all, delete")

    # For FileStorage
    def cities(self):
        return [city for city in self.cities
                if city.state_id == self.id]


HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
HBNB_ENV = os.environ.get('HBNB_ENV')
engine = create_engine(
    'mysql+mysqldb://{}:{}@{}/{}'.format(
        HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
Base.metadata.create_all(engine)
