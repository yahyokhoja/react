from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_orders():
    return {"message": "List of orders"}