import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, unique=False, default=True)
    role_id = Column(Integer,ForeignKey('role.id'))
    
    

class Role(Base):
    __tablename__ = 'role'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user = relationship(User)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250)) 
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250)) 
    diameter = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    gravity = Column(String(250))
    rotation_period = Column(String(250))
    
class PeoplePlanet(Base):
    __tablename__ = 'people_planet'
    id = Column(Integer, primary_key=True)
    id_people = Column(Integer, ForeignKey('people.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    people = relationship(People)
    planet = relationship(Planet)

class User_role(Base):
    __tablename__ = 'user_role'
    id = Column(Integer, primary_key=True)
    id_role = Column(Integer, ForeignKey('role.id'))
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    role = relationship(Role)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    p_p_id = Column(Integer,ForeignKey('people_planet.id'))
    user = relationship(User)
    p_p = relationship(PeoplePlanet)


class User_favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    id_favorites = Column(Integer, ForeignKey('favorites.id'))
    id_user = Column(Integer, ForeignKey('user.id'))
    favorites = relationship(User)
    user = relationship(Favorites)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')