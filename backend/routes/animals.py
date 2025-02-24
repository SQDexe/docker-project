from models import Animals
from dependencies import authenticate_user_dep, session_dep

from fastapi import APIRouter, HTTPException
from sqlmodel import select, update


router = APIRouter(prefix='/animals', tags=['animals'], dependencies=(authenticate_user_dep, ))

@router.get('/', status_code=200)
async def view_animals(session: session_dep):
    return session.exec(select(Animals)).all()

@router.post('/add', status_code=201)
async def add_animals(adoption: Animals, session: session_dep):
    session.add(adoption)
    session.commit()

@router.get('/edit/{id}', status_code=200)
async def preview_animals(id: int, session: session_dep):
    if animal := session.get(Animals, id):
        return animal
    raise HTTPException(status_code=404, detail='Animal not found')

@router.patch('/edit/{id}', status_code=204)
async def edit_animals(new: Animals, id: int, session: session_dep):
    if session.get(Animals, id):
        session.exec(update(Animals).where(Animals.id == id).values(**new.model_dump()))
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Animal not found')

@router.delete('/delete/{id}', status_code=204)
async def delete_animals(id: int, session: session_dep):
    if animal := session.get(Animals, id):
        session.delete(animal)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Animal not found')