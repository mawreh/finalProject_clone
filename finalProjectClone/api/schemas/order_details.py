from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer

class OrderDetail(BaseModel):  # Define OrderDetail before Order class
    order_id: int
    menu_id: int
    quantity: int

    class Config:
        orm_mode = True

class OrderDetailCreate(BaseModel):
    order_id: int
    menu_id: int
    quantity: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_id: int
    order_date: datetime
    tracking_number: str
    order_status: str
    total_price: float

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None

class Order(OrderBase):
    id: int
    customer: Customer = None
    order_details: list['OrderDetail'] = None  # Use quotes for forward reference

    class Config:
        from_attributes = True
