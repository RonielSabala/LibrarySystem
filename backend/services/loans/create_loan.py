from datetime import datetime

from backend.domain import Loan
from backend.domain.enums import BookStatusEnum
from backend.repository.loan_repository import LoanRepository
from backend.repository.book_repository import BookRepository
from backend.repository.student_repository import StudentRepository


def make_loan(
    book_id: int,
    student_id: int,
    end_date: datetime,
) -> None:

    loan_repository = LoanRepository()
    book_repository = BookRepository()
    student_repository = StudentRepository()

    book = book_repository.get_by_id(book_id)
    if not book:
        raise ValueError(f"Book with id {book_id} does not exist.")

    if book.status == BookStatusEnum.LOANED:
        raise ValueError("Book is already loaned.")

    student = student_repository.get_by_id(student_id)
    if not student:
        raise ValueError(f"Student with id {student_id} does not exist.")

    loan = Loan(
        book_id=book_id,
        student_id=student_id,
        end_date=end_date,
    )

    loan_repository.add(loan)

    book.status = BookStatusEnum.LOANED
    book_repository.update(book)
