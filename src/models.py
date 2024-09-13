import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table Character
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))


class Ship(Base):
    __tablename__ = 'Ship'
    # Here we define columns for the table Ship
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    population = Column(String(250))
    orbital_period = Column(String(250))
    rotation_period = Column(String(250))
    diameter = Column(String(250))

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    crew = Column(Integer)

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class User_character(Base):
    __tablename__ = 'User_character'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Character_id = Column(Integer, ForeignKey('Character.id'))
    Character = relationship(Character)

class User_Planet(Base):
    __tablename__ = 'User_Planet'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Planet_id = Column(Integer, ForeignKey('Planet.id'))
    Planet = relationship(Planet)

class User_Ship(Base):
    __tablename__ = 'User_Ship'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Ship_id = Column(Integer, ForeignKey('Ship.id'))
    Ship = relationship(Ship)

class Character_Ship(Base):
    __tablename__ = 'Character_Ship'
    # Here we define columns for the table Character
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Character_id = Column(Integer, ForeignKey('Character.id'))
    Character = relationship(Character)
    Ship_id = Column(Integer, ForeignKey('Ship.id'))
    Ship = relationship(Ship)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
