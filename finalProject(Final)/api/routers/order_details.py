from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from api.schemas.order_details import OrderDetailCreate, OrderDetail  # Add this import statement
from ..controllers import order_details as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)

@router.post("/", response_model=OrderDetailCreate)
def create_order_detail(request: OrderDetailCreate, db: Session = Depends(get_db)):
    new_order_detail = controller.create(request=request, db=db)
    return new_order_detail

@router.get("/", response_model=list[OrderDetail])
def read_all_order_details(db: Session = Depends(get_db)):
    order_details = controller.read_all(db=db)
    return order_details

@router.get("/{item_id}", response_model=OrderDetail)
def read_one_order_detail(item_id: int, db: Session = Depends(get_db)):
    order_detail = controller.read_one(item_id=item_id, db=db)
    if order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail not found")
    return order_detail

@router.put("/{item_id}", response_model=OrderDetail)
def update_order_detail(item_id: int, request: OrderDetailCreate, db: Session = Depends(get_db)):
    updated_order_detail = controller.update(item_id=item_id, request=request, db=db)
    if updated_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail not found")
    return updated_order_detail

@router.delete("/{item_id}")
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    deleted_order_detail = controller.delete(item_id=item_id, db=db)
    if deleted_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order Detail not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
