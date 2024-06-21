from athletes.models import Athlete
from database import get_session


def save_athlete(
    session,
    first_name,
    last_name,
    dob,
    bio=None,
):
    athlete = Athlete(first_name=first_name, last_name=last_name, dob=dob, bio=bio)
    session.add(athlete)
    session.commit()
    return athlete

def get_athletes(session):
    return session.query(Athlete).all()

def get_athlete_by_id(session, athlete_id):
    return session.query(Athlete).filter_by(id=athlete_id).first()

def update_athlete_by_id(session, athlete_id, **kwargs):
    athlete = session.query(Athlete).filter_by(id=athlete_id).first()
    if athlete:
        for key, value in kwargs.items():
            if hasattr(athlete, key):
                setattr(athlete, key, value)
        session.commit()
        return athlete
    return False

def delete_athlete_by_id(session, athlete_id):
    athlete = session.query(Athlete).filter_by(id=athlete_id).first()
    if athlete:
        session.delete(athlete)
        session.commit()
        return True
    return False
