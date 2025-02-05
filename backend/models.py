from typing import Optional
from decimal import Decimal
from datetime import date as Date

from pydantic import BaseModel, PositiveInt
from sqlmodel import SQLModel, Field, Enum


sha256_pattern, phone_num_pattern, email_pattern = (
    r'^[a-fA-F0-9]{64}$',
    r'^\d{64}$',
    r'^[\w\.-]+@[\w-]+\.[a-zA-Z]{2,4}$'
    )

class Login(BaseModel):
    username: str = Field(min_length=4, max_length=16)
    password_hash: str = Field(min_length=64, max_length=64, schema_extra={'pattern': sha256_pattern})

class Adoptions(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    date: Date = Field(ge=Date(1901, 1, 1), le=Date(2155, 12, 31))
    animal_id: PositiveInt = Field(foreign_key='animals.id', gt=0)
    signature: str = Field(max_length=100)

class Animals(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    species: str = Enum('dog', 'cat', 'lizard', 'bird', 'rodent')
    gender: str = Enum('male', 'female')
    birth: int = Field(ge=1901, le=2155)
    arrival: Date = Field(ge=Date(1901, 1, 1), le=Date(2155, 12, 31))

class Donations(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    date: Date = Field(ge=Date(1901, 1, 1), le=Date(2155, 12, 31))
    amount: Decimal = Field(ge=Decimal(0), le=Decimal(999999999), max_digits=11, decimal_places=2)
    signature: str = Field(max_length=100)

class Workers(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    username: str = Field(min_length=4, max_length=16)
    password_hash: str = Field(min_length=64, max_length=64, schema_extra={'pattern': sha256_pattern})
    admin: bool
    phone_number: str = Field(min_length=9, max_length=9, schema_extra={'pattern': phone_num_pattern})
    email: str = Field(max_length=50, schema_extra={'pattern': email_pattern})