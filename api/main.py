from fastapi import FastAPI
from api.routes import root, blog_post

app = FastAPI()

app.include_router(root.router)
app.include_router(blog_post.router)