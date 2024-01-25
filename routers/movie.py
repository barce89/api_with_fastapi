from fastapi import APIRouter
from fastapi import Path,Query,Depends
from fastapi.responses import JSONResponse
from typing import Any, Optional,List
from config.data import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schema.movie import Movie


movie_router = APIRouter()



#,dependencies=[Depends(JWTBearer())]
@movie_router.get('/movies',tags = ['movies'],response_model=List[Movie],status_code=200)
def get_movies()->List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code = 200,content = jsonable_encoder(result))

@movie_router.get('/movies/{id}',tags = ['movies'],response_model=Movie)
def get_movie(id:int = Path(ge=1,le=2000))->Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code= 404,content={'message':'Pelicula no encontrada'})  
    return JSONResponse(status_code = 200,content = jsonable_encoder(result))  
    

@movie_router.get('/movies/',tags = ['movies'],response_model=List[Movie])
def get_movies_by_category(category:str = Query(min_length=5,max_length=15))->List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code= 404,content={'message':'Pelicula no encontrada'})  
    return JSONResponse(status_code = 200,content = jsonable_encoder(result))  
    

@movie_router.post('/movies',tags= ['movies'],response_model=dict,status_code = 201)
def create_movie(movie:Movie)->dict:
    #print("Data received:", movie.model_dump())
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code = 201,content = {'message':'Se ha registrado la pelicula'})

@movie_router.put('/movies/{id}',tags = ['movies'],response_model=dict,status_code = 200)
def update_movies(id:int,movie:Movie)->dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404,content = {'message':'No encontrado'})

    MovieService(db).update_movies(id,movie)
    return JSONResponse(status_code = 200,content = {'message':'Se ha modificado la pelicula'})


@movie_router.delete('/movies/{id}',tags = ['movies'],response_model=dict,status_code = 200)
def remove_movie(id:int)->dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code= 404,content={'message':'Pelicula no encontrada'})

    MovieService(db).remove_movie(id)
    return JSONResponse(status_code = 200,content = {'message':'Se ha eliminado la pelicula'})
