#!/usr/bin/python3
"""Database Engine"""
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

from models.base_model import BaseModel, Base


class DBStorage:
    """Defining the Database"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB')
        HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST')
        HBNB_ENV = os.environ.get('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        self.__session = Session(bind=self.__engine)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        session = self.__session
        return_dict = {}
        if cls is None:
            from models.amenity import Amenity
            from models.state import State
            from models.user import User
            from models.city import City
            from models.review import Review
            from models.place import Place
            queries = [session.query(User).all(), session.query(State).all(),
                       session.query(City).all(), session.query(Amenity).all(),
                       session.query(Place).all(), session.query(Review).all()]
            for query in queries:
                for row in query:
                    obj_id = "{}.{}".format(row.__class__.__name__, row.id)
                    if hasattr(row, '_sa_instance_state'):
                        delattr(row, '_sa_instance_state')
                    return_dict[obj_id] = row
        else:
            rows = session.query(cls).all()
            for row in rows:

                obj_id = "{}.{}".format(row.__class__.__name__, row.id)
                if hasattr(row, '_sa_instance_state'):
                    delattr(row, '_sa_instance_state')
                return_dict[obj_id] = row
        return return_dict

    def new(self, obj):
        """Create new db object"""
        self.__session.add(obj)

    def save(self):
        """Commit new change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.amenity import Amenity
        from models.state import State
        from models.user import User
        from models.city import City
        from models.review import Review
        from models.place import Place
        Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
