from models import Workers
from dependencies import authenticate_admin_dep, session_dep

from fastapi import APIRouter, HTTPException
from sqlmodel import select, update


router = APIRouter(prefix='/workers', tags=['workers'], dependencies=(authenticate_admin_dep, ))

@router.get('/', status_code=200)
async def view_workers(session: session_dep) -> list[Workers]:
    return session.exec(select(Workers)).all()

@router.post('/add', status_code=201)
async def add_workers(adoption: Workers, session: session_dep):
    session.add(adoption)
    session.commit()

@router.get('/edit/{id}', status_code=200)
async def preview_workers(id: int, session: session_dep):
    if worker := session.get(Workers, id):
        return worker
    raise HTTPException(status_code=404, detail='Worker not found')

@router.patch('/edit/{id}', status_code=204)
async def edit_workers(new: Workers, id: int, session: session_dep):
    if session.get(Workers, id):
        session.exec(update(Workers).where(Workers.id == id).values(**new.model_dump()))
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Worker not found')

@router.delete('/delete/{id}', status_code=204)
async def delete_workers(id: int, session: session_dep):
    if worker := session.get(Workers, id):
        session.delete(worker)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail='Worker not found')