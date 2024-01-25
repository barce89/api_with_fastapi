from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title : str = Field(default= 'Mi pelicula',min_length=5,max_Length = 15)
    overview : str = Field(default= 'descripcion de la pelicula',min_length=15,max_Length = 50)
    year : int = Field(default= 2022,le=2022)
    rating : float = Field(ge= 0,le=10)
    category : str = Field(min_length=3,max_Length = 15)

    class Config:
        json_schema_extra = {
            "example":{
                'id':1,
                'title':"Mi pelicula",
                'overview':'Descripcion de la peli',
                'year':2022,
                'rating':9.8,
                'category': "Accion"

            }
        }