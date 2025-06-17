from fastapi import APIRouter
from config.db import SessionLocal
from models.user import users
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

from cryptography.fernet import Fernet

user = APIRouter()

@user.get('/users')
def get_users():
    return SessionLocal.execute(users.select()).fetchall()

@user.get('/users')
def helloworld():
    return "Hello Users!"

@user.get('/users')
def helloworld():
    return "Hello Users!"

@user.get('/users')
def helloworld():
    return "Hello Users!"

@user.get('/users')
def helloworld():
    return "Hello Users!"