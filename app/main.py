from fastapi import FastAPI, Request, Path, HTTPException
from typing import Annotated
from app.routes import todo                 # app ke andr routes package tha, uske andr todo file thi
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()

app.include_router(todo.router)             # Telling our app that we've created routes there

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = {}

    for error in exc.errors():
        print(error)
        errors[error['loc'][-1]] = error['msg']

    return JSONResponse(
        {"Message": "Validation Error", "errors":errors}, status_code=422 
    )



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





