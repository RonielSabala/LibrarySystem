from dataclasses import dataclass


@dataclass(slots=True, kw_only=True, frozen=True)
class Student:
    student_id: int
    student_name: str
