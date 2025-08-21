import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.blog_post.repository.blog_post_repository import BlogPostRepository
from app.core.database.db import Base


@pytest.fixture
def test_engine():
    """Cria um engine SQLite em memória para testes"""
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    return engine


@pytest.fixture
def test_session(test_engine):
    """Cria uma sessão de teste que faz rollback após cada teste"""
    session = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)()
    yield session
    session.close()


@pytest.fixture
def test_repository(test_session):
    """Cria um repositório usando a sessão de teste"""
    repo = BlogPostRepository(test_session)
    return repo 