from fastapi import APIRouter

from .athletes import router as athletes_router

router = APIRouter(prefix="/v1")
router.include_router(athletes_router)
