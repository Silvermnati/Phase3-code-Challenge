from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    food_entries = relationship("FoodEntry", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    meal_plans = relationship("MealPlan", back_populates="user")

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    calories = Column(Integer)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="food_entries")

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    daily_calories = Column(Integer)
    weekly_calories = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="goals")

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True)
    week_number = Column(Integer)
    plan_details = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="meal_plans")