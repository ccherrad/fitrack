from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session


from core.database import get_session
from crud.athletes import (
    save_athlete,
    get_athletes,
)
from schemas.athletes import AthleteIn, AthleteOut


router = APIRouter(
    prefix="/athletes", responses={401: {"description": "User is not authenticated."}}
)

@router.post(
    "/",
    tags=["Athletes"],
    status_code=200,
    response_model=AthleteOut,
)
def create_athlete(
    athlete_in: AthleteIn,
    session: Session = Depends(get_session),
):
    athlete = save_athlete(
                session,
                athlete_in.fullname,
                athlete_in.dob,
                athlete_in.bio,
                athlete_in.group_id,
            )
    return athlete


@router.get(
    "/",
    tags=["Athletes"],
    status_code=200,
    response_model=List[AthleteOut],
)
def get_all_athletes(
    session: Session = Depends(get_session),
):
    athletes = get_athletes(session)
    return athletes
