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
        return_vals = {}
        if cls is None:
            from models.amenity import Amenity
            from models.state import State
            from models.user import User
            from models.city import City
            from models.review import Review
            from models.place import Place
            return {
                f'{User.__class__name}.{User.id}': session.query(User).all(),
                f'{State.__class__name}.{State.id}': session.query(State).all(),
                f'{City.__class__name}.{City.id}': session.query(City).all(),
                f'{Amenity.__class__name}.{Amenity.id}': session.query(Amenity).all(),
                f'{Place.__class__name}.{Place.id}': session.query(Place).all(),
                f'{Review.__class__name}.{Review.id}': session.query(Review).all()
            }
        return {'{}.{}'.format(cls.__name__, cls.id): row}

    def new(self, obj):
        """Create new db object"""
        session = self.__session
        session.add(obj)

    def save(self):
        """Commit new change"""
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
