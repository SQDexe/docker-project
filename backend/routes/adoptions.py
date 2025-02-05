from models import Adoptions
from dependencies import authenticate_user_dep, session_dep

from fastapi import APIRouter, HTTPException
from sqlmodel import select, update


router = APIRouter(prefix='/adoptions', tags=['adoptions'], dependencies=[authenticate_user_dep])

@router.get('/', status_code=200)
async def view_adoptions(session: session_dep):
    return session.exec(select(Adoptions)).all()

@router.post('/add', status_code=201)
async def add_adoptions(adoption: Adoptions, session: session_dep):
    session.add(adoption)
    session.commit()

@router.get('/edit/{id}', status_code=200)
async def preview_adoptions(id: int, session: session_dep):
    if adoption := session.get(Adoptions, id):
        return adoption
    raise HTTPException(status_code=404, detail='Adoption not found')

@router.patch('/edit/{id}', status_code=204)
async def edit_adoptions(new: Adoptions, id: int, session: session_dep):
    if session.get(Adoptions, id):
        session.exec(update(Adoptions).where(Adoptions.id == id).values(**new.model_dump()))
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Adoption not found')

@router.delete('/delete/{id}', status_code=204)
async def delete_adoptions(id: int, session: session_dep):
    if adoption := session.get(Adoptions, id):
        session.delete(adoption)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Adoption not found')