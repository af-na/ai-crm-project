from sqlalchemy import Column, Integer, String, Text
from database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hp_name = Column(String(100), index=True)
    specialty = Column(String(100), index=True)
    notes = Column(Text)
