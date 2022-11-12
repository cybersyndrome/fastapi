from fastapi import FastAPI, APIRouter
from todo import todo_router
from model import Todo

app = FastAPI()

#define decorator to indicate the type of operation
#followed by a functiom containing the operation to be carried out 


@app.get("/")
async def welcome() -> dict:
    '''this function is a route handler for processing the requests/response'''

    return { "message": " Hello world"}

#Uvicorn cannnot use the apirouter instance to serve the application
# routes defined using the APIRouter class are added to the FastAPI instance to enable their visibility
# the method below is responsible for adding routes to the main apps instance to enable the routes to become visibles
app.include_router(todo_router) 