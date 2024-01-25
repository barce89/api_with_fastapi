from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schema.user import User

user_router = APIRouter()



@user_router.post('/login',tags = ['auth'])
def login(user:User):
    if user.email == "fulano@hotmail.com" and user.password == "admin":
        token :str = create_token(user.model_dump())
        return JSONResponse(status_code=200,content = token)
    else:
        return f'Uno de los campos esta incorrecto'