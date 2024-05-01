from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_email = Column(String(100))
    customer_number = Column(String(100))
    customer_address = Column(String(100))
