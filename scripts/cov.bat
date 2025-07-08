@echo off
uv run pytest --cov=api --cov-report=term-missing > logs/cov.txt