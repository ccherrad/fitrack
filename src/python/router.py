from fastapi import APIRouter

from athletes.router import router as athlete_router

router = APIRouter(prefix="/api/v1")
router.include_router(athlete_router)
