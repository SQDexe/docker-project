from models import Login, Animals, Workers
from dependencies import create_token, authenticate_user_dep, session_dep

from fastapi import APIRouter, HTTPException
from sqlmodel import select, and_


router = APIRouter()

@router.post('/login', tags=['login'], status_code=200)
async def login(login: Login, session: session_dep):
    try:
        username, is_admin = session.exec(
            select(Workers.username, Workers.admin).where(and_(Workers.username == login.username, Workers.password_hash == login.password_hash))
            ).one()

    except Exception as e:
        raise HTTPException(status_code=401, detail=f'Authentication failed')
    
    return { 'access_token': create_token(username, is_admin), 'token_type': 'bearer' }


@router.get('/data/adoptions', tags=['data', 'adoptions'], dependencies=[authenticate_user_dep], status_code=200)
async def get_data_adoption(session: session_dep):
    return { 'animal_ids': session.exec(select(Animals.id)).all() }

@router.get('/data/animals', tags=['data', 'animals'], dependencies=[authenticate_user_dep], status_code=200)
async def get_data_animals():
    return {
        'species': ('dog', 'cat', 'lizard', 'bird', 'rodent'),
        'gender': ('male', 'female')
        }