@echo off
uv run pytest --cov=api --cov-report=term-missing > tests/result.txt