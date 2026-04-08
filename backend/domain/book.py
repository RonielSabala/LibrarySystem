from dataclasses import dataclass, field

from domain.enums.book_status_enum import BookStatusEnum


@dataclass(slots=True, kw_only=True)
class Book:
    book_id: int
    title: str
    author_name: str
    author_surname: str
    category: str
    publisher: str
    section: int
    status: BookStatusEnum = field(default=BookStatusEnum.ON_LIBRARY, init=False)
