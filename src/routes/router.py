from fastapi import APIRouter
from src.api.v1.main import view
router = APIRouter(prefix="/api/v1")
 
router.include_router(view.router)