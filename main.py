
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.data import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from services.movie import MovieService


app = FastAPI()
app.title = 'Mi aplicacion con fastApi'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind = engine)


movies = [{
    "id":1,
    "title":"Avatar",
    "overview":'En un exuberante planeta llamado pandora viven los ',
    "year": "2009",
    "rating": 7.8,
    "category": "Accion"

},{
    "id":2,
    "title":"titanic",
    "overview":'un joven pintor se embarca en  ',
    "year": "2005",
    "rating": 7.8,
    "category": "Romance"

}
]


@app.get('/',tags = ['home'])
def message():
    return HTMLResponse('<h1>hello world</h1>')

#if __name__ == '__main__':