from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from core.database.db import Base


class BlogPostEntity(Base):
    __tablename__ = "blog_posts"

    post_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC))