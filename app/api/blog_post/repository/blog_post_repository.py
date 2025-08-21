from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.api.blog_post.entities.blog_post_entity import BlogPostEntity
from app.api.blog_post.errors.blog_post_errors import PostNotFoundError
from app.api.blog_post.interfaces.blog_post_interface import IBlogPostRepository
from app.api.blog_post.models.blog_post_models import BlogPost, BlogPostCreate, BlogPostPatch, BlogPostUpdate


class BlogPostRepository(IBlogPostRepository):
    def __init__(self, session: Session):
        self.session = session

    def _get_current_datetime(self) -> datetime:
        return datetime.now(UTC)

    def create_blog_post(self, blog_post: BlogPostCreate) -> BlogPost:
        db_post = BlogPostEntity(
            title=blog_post.title,
            content=blog_post.content,
            author=blog_post.author,
            created_at=self._get_current_datetime(),
            updated_at=self._get_current_datetime(),
        )
        self.session.add(db_post)
        self.session.commit()
        self.session.refresh(db_post)
        return BlogPost(
            post_id=db_post.post_id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            created_at=db_post.created_at,
            updated_at=db_post.updated_at
        )

    def update_blog_post(self, post_id: int, blog_post: BlogPostUpdate) -> BlogPost:
        db_post = self.session.get(BlogPostEntity, post_id)
        if db_post is None:
            raise PostNotFoundError(post_id)

        db_post.title = blog_post.title
        db_post.content = blog_post.content
        db_post.author = blog_post.author
        db_post.updated_at = self._get_current_datetime()

        self.session.commit()
        return BlogPost(
            post_id=db_post.post_id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            created_at=db_post.created_at,
            updated_at=db_post.updated_at
        )

    def patch_blog_post(self, post_id: int, blog_post: BlogPostPatch) -> BlogPost:
        db_post = self.session.get(BlogPostEntity, post_id)
        if db_post is None:
            raise PostNotFoundError(post_id)

        if blog_post.title is not None:
            db_post.title = blog_post.title
        if blog_post.content is not None:
            db_post.content = blog_post.content
        if blog_post.author is not None:
            db_post.author = blog_post.author

        db_post.updated_at = self._get_current_datetime()
        self.session.commit()
        return BlogPost(
            post_id=db_post.post_id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            created_at=db_post.created_at,
            updated_at=db_post.updated_at
        )

    def delete_blog_post(self, post_id: int) -> int:
        db_post = self.session.get(BlogPostEntity, post_id)
        if db_post is None:
            raise PostNotFoundError(post_id)

        self.session.delete(db_post)
        self.session.commit()
        return post_id

    def get_blog_post(self, post_id: int) -> BlogPost:
        db_post = self.session.get(BlogPostEntity, post_id)
        if db_post is None:
            raise PostNotFoundError(post_id)
        return BlogPost(
            post_id=db_post.post_id,
            title=db_post.title,
            content=db_post.content,
            author=db_post.author,
            created_at=db_post.created_at,
            updated_at=db_post.updated_at
        )

    def get_all_blog_posts(self) -> list[BlogPost]:
        posts = self.session.query(BlogPostEntity).all()
        return [BlogPost(
            post_id=post.post_id,
            title=post.title,
            content=post.content,
            author=post.author,
            created_at=post.created_at,
            updated_at=post.updated_at
        ) for post in posts]
