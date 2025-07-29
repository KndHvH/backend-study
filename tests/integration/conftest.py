import os
import tempfile
import time

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.main import app
from core.database.db import Base, get_db


@pytest.fixture(scope="function")
def test_client():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp_file:
        test_db_path = f"sqlite:///{tmp_file.name}"
        tmp_file_name = tmp_file.name
    
    test_engine = create_engine(test_db_path, connect_args={"check_same_thread": False})
    test_session_local = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    
    Base.metadata.create_all(bind=test_engine)
    
    def override_get_db():
        db = test_session_local()
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    
    client = TestClient(app)
    
    yield client
    
    app.dependency_overrides.clear()
    test_engine.dispose()
    
    for _ in range(3):
        try:
            os.unlink(tmp_file_name)
            break
        except PermissionError:
            time.sleep(0.1)
        except FileNotFoundError:
            break