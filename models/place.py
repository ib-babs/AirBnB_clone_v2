#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Float, Column, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # Building relationship with the Review object
    # FOR DBStorage
    reviews = relationship('Review', backref='place',
                           cascade='all, delete, delete-orphan')
    # For FileStorage

    @property
    def reviews(self):
        return [review for review in self.reviews
                if review.state_id == self.id]

    # Creating the relationship Many-To-Many between Place and Amenity:
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60), ForeignKey(
                              'places.id'), nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False))

    amenities = relationship(
        'Amenity', secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        print(self.amenities)
        return [amenity for amenity in self.amenities
                if amenity.state_id == self.id]

    # @property.setter
    # def amenities(self, obj):
    #     if obj.__class__.__name__ == 'Amenity':
    #         self.amenities
