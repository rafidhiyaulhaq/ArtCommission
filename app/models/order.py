from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from ..database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    artist_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    status = Column(String)  # pending/in-progress/completed
    created_at = Column(DateTime(timezone=True), server_default=func.now())