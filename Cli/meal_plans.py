class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True)
    week_number = Column(Integer)
    plan_details = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="meal_plans")