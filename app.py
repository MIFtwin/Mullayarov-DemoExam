from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated
import datetime

app = FastAPI()

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str

repo = []

@app.post("/orders")
def create_order(
    number: Annotated[int, Form()],
    startDate: Annotated[datetime.date, Form()],
    device: Annotated[str, Form()],
    problemType: Annotated[str, Form()],
    description: Annotated[str, Form()],
    client: Annotated[str, Form()],
    status: Annotated[str, Form()],
):
    order = Order(
        number=number,
        startDate=startDate,
        device=device,
        problemType=problemType,
        description=description,
        client=client,
        status=status,
    )
    repo.append(order)
    return {"message": "Order created successfully"}

@app.get("/orders")
def get_orders():
    return repo

