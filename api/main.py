from fastapi import FastAPI
from api.routes import root 

app = FastAPI()

app.include_router(root.router)