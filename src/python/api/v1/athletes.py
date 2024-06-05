from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session


from core.database import get_session
from crud.athletes import (
    save_athlete,
    get_athletes,
    get_athlete_by_id,
    update_athlete_by_id,
    delete_athlete_by_id,
)
from schemas.athletes import AthleteIn, AthleteOut, AthleteUpdate


router = APIRouter(
    prefix="/athletes", responses={401: {"description": "User is not authenticated."}}
)

@router.post(
    "/",
    tags=["Athletes"],
    status_code=status.HTTP_201_CREATED,
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
    status_code=status.HTTP_200_OK,
    response_model=List[AthleteOut],
)
def get_all_athletes(
    session: Session = Depends(get_session),
):
    athletes = get_athletes(session)
    return athletes

@router.get(
    "/{id}",
    tags=["Athletes"],
    status_code=status.HTTP_200_OK,
    response_model=AthleteOut,
)
def get_athlete(
    id: int,
    session: Session = Depends(get_session),
):
    athlete = get_athlete_by_id(session, id)
    return athlete

@router.put(
    "/{id}",
    tags=["Athletes"],
    status_code=status.HTTP_200_OK,
    response_model=AthleteOut,
)
def update_athlete(
    id: int,
    athlete_update: AthleteUpdate,
    session: Session = Depends(get_session),
):
    athlete = update_athlete_by_id(session, id, **athlete_update.model_dump(exclude_none=True))
    return athlete


@router.delete(
    "/{id}",
    tags=["Athletes"],
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_athlete(
    id: int,
    session: Session = Depends(get_session),
):
    return delete_athlete_by_id(session, id)
