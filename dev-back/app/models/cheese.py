from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Cheese(Base):
    __tablename__ = "cheeses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    description = Column(Text, nullable=False)
    origin = Column(String(100))
    milk_type = Column(String(50))  # vache, chèvre, brebis, etc.
    price_per_kg = Column(Float, nullable=False)
    image_url = Column(String(255))
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
