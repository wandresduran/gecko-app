from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def heath_check():
    return {"status":"ok"}