from dataclasses import dataclass
from typing import Any, Union, Optional


@dataclass
class Sample:
    id: int | None = None
    time: str | None = None
    user_id: int | None = None
    text: str | None = None
