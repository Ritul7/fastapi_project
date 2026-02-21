from fastapi import FastAPI, Request, Path
from typing import Annotated

app = FastAPI()

# @app.get('/')
# def root():
#     return {"Message": "Everything is running"}

@app.get('/')
def get_name(request: Request):
    params = request.query_params
    return {"Message": params }

@app.get('/items/{id}')
def get_items(id: Annotated[int, Path(ge=0)]):
    return {"Id is": id}
# def get_items(id: int):
#     return f"Id is {id}"





