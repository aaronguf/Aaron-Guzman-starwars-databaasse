import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er
from sqlalchemy import DateTime
from datetime import datetime

Base = declarative_base()

# Many to Many
favorited_vehicles=Table('favorite_vehicles',Base.metadata,
                        Column('user_id',Integer,(ForeignKey('user.id'))),
                        Column('vehicles_id',Integer,(ForeignKey('vehicles.id')))
                         )

class FavoriteCharacter(Base):
    __tablename__='favorite_characters'
    id=Column(Integer,primary_key=True)
    created_at=Column(DateTime,default=datetime.utcnow)

    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='favorited_by')
    character_id=Column(Integer,ForeignKey('character.id'))
    character=relationship('Characters',back_populates='favorite_characters')


# Explicit Association Model
class FavoritePlanets(Base):
    __tablename__='favorite_planets'
    id=Column(Integer,primary_key=True)
    created_at=Column(DateTime,default=datetime.utcnow)


    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='favorited_by')

    planets_id=Column(Integer,ForeignKey('planets.id'))
    planets=relationship('Planets',back_populates='favorite_planets')


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_status=Column(String(250), nullable=False)
    email=Column(String(250),nullable=False)

    favorited_by_characters=relationship('FavoriteCharacters',back_populates='user')
    favorited_by_planets=relationship('FavoritePlanets',back_populates='planets')
    favorited_by_vehicles=relationship('Vehicles', secondary=favorited_vehicles, back_populates='favorited_by')

class Characters(Base):
    __tablename__='character'
    id=Column(Integer,primary_key=True)
    name=Column(String(250))
    color_hair=Column(String(250))
    age=Column(Integer)
    height=Column(Integer)
    favorite_characters=relationship('FavoriteCharacters',back_populates='character')
    
    
class Planets(Base):
    __tablename__='planets'
    id=Column(Integer,primary_key=True)
    name=Column(String(250))
    atmosphere=Column(String(250))
    diameter=Column(Integer)
    rotation=Column(Integer)
    orbital=Column(Integer)
    favorite_planets=relationship('FavoritePlanets',back_populates='planets')

class Vehicles(Base):
    __tablename__='vehicles'
    id=Column(Integer,primary_key=True)
    model=Column(String(250))
    vehicles=Column(String(250))
    length=Column(String(250))
    crew=Column(Integer)
    passengers=Column(Integer)

    favorite_vehicles=relationship('Vehicles',secondary=favorited_vehicles,back_populates='favorite_vehicles')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
