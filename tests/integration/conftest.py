import contextlib
import os
import tempfile
import time

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from api.main import app
from core.database.db import Base


@pytest.fixture(scope="function")
def test_client():
    """Cliente de teste que usa banco SQLite temporário"""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp_file:
        test_db_path = f"sqlite:///{tmp_file.name}"
        tmp_file_name = tmp_file.name
    
    original_db_path = os.environ.get("DB_PATH")
    original_environment = os.environ.get("ENVIRONMENT")
    os.environ["DB_PATH"] = test_db_path
    os.environ["ENVIRONMENT"] = "test"
    

    test_engine = create_engine(test_db_path, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=test_engine)
    
    client = TestClient(app)
    
    yield client
    
    test_engine.dispose()
    
    if original_db_path:
        os.environ["DB_PATH"] = original_db_path
    else:
        os.environ.pop("DB_PATH", None)
    
    if original_environment:
        os.environ["ENVIRONMENT"] = original_environment
    else:
        os.environ.pop("ENVIRONMENT", None)
    
    for _ in range(3):
        try:
            os.unlink(tmp_file_name)
            break
        except PermissionError:
            time.sleep(0.1)
        except FileNotFoundError:
            break