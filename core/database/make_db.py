from api.domains.blog_post.entities.blog_post_entity import BlogPostEntity  # noqa: F401
from core.database.db import Base, engine

Base.metadata.create_all(bind=engine)