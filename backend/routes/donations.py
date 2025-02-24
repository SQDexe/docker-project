from models import Donations
from dependencies import authenticate_user_dep, session_dep

from fastapi import APIRouter, HTTPException
from sqlmodel import select, update


router = APIRouter(prefix='/donations', tags=['donations'], dependencies=(authenticate_user_dep, ))

@router.get('/', status_code=200)
async def view_donations(session: session_dep):
    return session.exec(select(Donations)).all()

@router.post('/add', status_code=201)
async def add_donations(adoption: Donations, session: session_dep):
    session.add(adoption)
    session.commit()

@router.get('/edit/{id}', status_code=200)
async def preview_donations(id: int, session: session_dep):
    if donation := session.get(Donations, id):
        return donation
    raise HTTPException(status_code=404, detail='Donation not found')

@router.patch('/edit/{id}', status_code=204)
async def edit_donations(new: Donations, id: int, session: session_dep):
    if session.get(Donations, id):
        session.exec(update(Donations).where(Donations.id == id).values(**new.model_dump()))
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Donation not found')

@router.delete('/delete/{id}', status_code=204)
async def delete_donations(id: int, session: session_dep):
    if donation := session.get(Donations, id):
        session.delete(donation)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Donation not found')