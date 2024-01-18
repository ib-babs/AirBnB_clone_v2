#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    # # Creating the relationship Many-To-Many between Place and Amenity:
    # metadata = Base.metadata
    # place_amenity = Table('place_amenity', metadata,
    #                       Column('place_id', String(60), ForeignKey(
    #                           'places.id'),  nullable=False),
    #                       Column('amenity_id', String(60), ForeignKey('amenities.id'),  nullable=False))
    place_amenities = relationship(
        'Place', secondary='place_amenity', viewonly=False)
