from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")

class ResponseModel(BaseModel, T):
	success: bool
	message: str
	data: T | None