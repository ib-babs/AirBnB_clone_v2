#!/usr/bin/python3
"""Database Engine"""
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os


class DBStorage:
    """Defining the Database"""
    __engine = None
    __session = None
    Base = declarative_base()

    def __init__(self) -> None:
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_ENV = os.environ.get('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            self.Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        self.__session = Session(bind=self.__engine)

        session = self.__session
        row = session.query(cls).all()
        # return_vals = {}
        # if cls is None:
        #     from models.amenity import Amenity
        #     from models.state import State
        #     from models.user import User
        #     from models.city import City
        #     from models.review import Review
        #     from models.place import Place
        #     rows = session.query()
        #     obj_id = state.State.__name__ + '.' + state.State.id
        #     obj_id = model.__class.__name + '.' + model.id
        #     return_vals[obj_id] = rows.all()
        #     return return_vals
        print(cls)
        return {'{}.{}'.format(cls.__name__, cls.id): row}

    def new(self, obj):
        """Create new db object"""
        session = self.__session
        session.add(obj)

    def save(self):
        """Commit new change"""
        print(self.__engine)
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.state import State
        from models.city import City
        self.Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
