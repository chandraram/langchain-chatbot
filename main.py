from fastapi import FastAPI
from pydantic import BaseModel

# Create the app instance
app = FastAPI()

# Define a request body model
class GreetRequest(BaseModel):
    name: str

# Define a simple GET route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI example!"}

# Define a POST route to greet a user
@app.post("/greet")
def greet_user(request: GreetRequest):
    return {"message": f"Hello, {request.name}!"}
