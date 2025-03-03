from typing import Any, Annotated
from collections.abc import Generator

from os import getenv
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jwt import encode, decode
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from sqlmodel import Session, create_engine
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


load_dotenv()

MARIADB_DATABASE, MARIADB_USER, MARIADB_PASSWORD = (
    getenv('MARIADB_DATABASE'),
    getenv('MARIADB_USER'),
    getenv('MARIADB_PASSWORD'),
    )
DB_HOSTNAME, DB_PORT, DB_CONNECTOR = (
    getenv('DB_HOSTNAME'),
    getenv('DB_PORT'),
    getenv('DB_CONNECTOR')
    )
JWT_KEY, JWT_ALGORITHM, JWT_EXPIRE_MINUTES = (
    getenv('JWT_KEY'),
    getenv('JWT_ALGORITHM'),
    int(getenv('JWT_EXPIRE_MINUTES'))
    )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
oauth2_dep = Depends(oauth2_scheme)

class NotAdminError(InvalidTokenError):
    'Raised when user in token isn\'t an admin'
    ...

def create_token(username: str, is_admin: bool) -> str:
    claims: dict[str, Any] = {
        'sub': username,
        'exp': datetime.now() + timedelta(minutes=JWT_EXPIRE_MINUTES),
        'adm': is_admin
        }
    return encode(claims, key=JWT_KEY, algorithm=JWT_ALGORITHM)

def break_token(token: str) -> dict[str, Any]:
    return decode(token, key=JWT_KEY, algorithms=[JWT_ALGORITHM])

def authenticate_user(token: str = oauth2_dep) -> None:
    try:
        break_token(token)
    except ExpiredSignatureError:
        raise HTTPException(status_code=440, detail='Session expired')
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail='Authentication failed')

def authenticate_admin(token: str = oauth2_dep) -> None:
    try:
        if not break_token(token)['adm']:
            raise NotAdminError()
    except NotAdminError:
        raise HTTPException(status_code=403, detail='No access rights')
    except ExpiredSignatureError:
        raise HTTPException(status_code=440, detail='Session expired')
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail='Authentication failed')


engine = create_engine(f'{DB_CONNECTOR}://{MARIADB_USER}:{MARIADB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{MARIADB_DATABASE}')

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_session)]
authenticate_user_dep = Depends(authenticate_user)
authenticate_admin_dep = Depends(authenticate_admin)
