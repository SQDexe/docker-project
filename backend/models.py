from typing import Optional
from decimal import Decimal
from datetime import date as Date

from pydantic import BaseModel, PositiveInt
from sqlmodel import SQLModel, Field, Enum


min_date, max_date = Date(1901, 1, 1), Date(2155, 12, 31)

sha256_pattern, phone_num_pattern, email_pattern = (
    r'^[a-fA-F0-9]{64}$',
    r'^\d{64}$',
    r'^[\w\.-]+@[\w-]+\.[a-zA-Z]{2,4}$'
    ) 

date_examples, year_examples, amount_examples = (
    (Date(2019, 6, 7), Date(2007, 4, 23), Date(2022, 10, 15)),
    (2008, 2024, 2021),
    (120.00, 5700.50, 69420.99)
    )
animal_name_examples, name_examples, surname_examples, signature_examples = (
    ('Sherlock', 'Polly', 'Felix'),
    ('Jane', 'Jan', 'John'),
    ('Doe', 'Kowalski', 'Smith'),
    ('Jane Doe', 'Jan Kowalski', 'John Smith')
    )
username_examples, phone_num_examples, email_examples = (
    ('joedoe', 'admin', 'work1'),
    ('123456789', '987654321', '333666999'),
    ('example@gmail.com', 'test@gmail.com', 'jane.doe@tf2.com')
    )

class Login(BaseModel):
    username: str = Field(min_length=4, max_length=16, schema_extra={'examples': username_examples})
    password_hash: str = Field(min_length=64, max_length=64, schema_extra={'pattern': sha256_pattern})

class Adoptions(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    date: Date = Field(ge=min_date, le=max_date, schema_extra={'examples': date_examples})
    animal_id: PositiveInt = Field(foreign_key='animals.id')
    signature: str = Field(max_length=100, schema_extra={'examples': signature_examples})

class Animals(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, schema_extra={'examples': animal_name_examples})
    species: str = Enum('dog', 'cat', 'lizard', 'bird', 'rodent')
    gender: str = Enum('male', 'female')
    birth: int = Field(ge=min_date.year, le=max_date.year, schema_extra={'examples': year_examples})
    arrival: Date = Field(ge=min_date, le=max_date, schema_extra={'examples': date_examples})

class Donations(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    date: Date = Field(ge=min_date, le=max_date, schema_extra={'examples': date_examples})
    amount: Decimal = Field(ge=Decimal(0), le=Decimal(999999999), max_digits=11, decimal_places=2, schema_extra={'examples': amount_examples})
    signature: str = Field(max_length=100, schema_extra={'examples': signature_examples})

class Workers(SQLModel, table=True):
    id: Optional[PositiveInt] = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, schema_extra={'examples': name_examples})
    surname: str = Field(max_length=50, schema_extra={'examples': surname_examples})
    username: str = Field(min_length=4, max_length=16, schema_extra={'examples': username_examples})
    password_hash: str = Field(min_length=64, max_length=64, schema_extra={'pattern': sha256_pattern})
    admin: bool
    phone_number: str = Field(min_length=9, max_length=9, schema_extra={'examples': phone_num_examples, 'pattern': phone_num_pattern})
    email: str = Field(max_length=50, schema_extra={'examples': email_examples, 'pattern': email_pattern})