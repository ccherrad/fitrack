from models.athletes import Athlete
from core.database import get_session


def save_athlete(
    session,
    fullname,
    dob,
    bio=None,
    group_id=None,
):
    athlete = Athlete(fullname=fullname, dob=dob, bio=bio, group_id=group_id)
    session.add(athlete)
    session.commit()
    return athlete

def get_athletes(session):
    return session.query(Athlete).all()

def get_athlete_by_id(session, athlete_id):
    return session.query(Athlete).filter_by(id=athlete_id).first()

def update_athlete(session, athlete_id, **kwargs):
    athlete = session.query(Athlete).filter_by(id=athlete_id).first()
    if athlete:
        for key, value in kwargs.items():
            if hasattr(athlete, key):
                setattr(athlete, key, value)
        session.commit()
        return True
    return False

def delete_athlete(session, athlete_id):
    athlete = session.query(Athlete).filter_by(id=athlete_id).first()
    if athlete:
        session.delete(athlete)
        session.commit()
        return True
    return False
