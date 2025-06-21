from fastapi import FastAPI
from api.routes import blog_post_routes, root

app = FastAPI()

app.include_router(root.router)
app.include_router(blog_post_routes.router)