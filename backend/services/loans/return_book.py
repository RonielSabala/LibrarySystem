from backend.domain.enums import LoanStatusEnum, BookStatusEnum
from backend.repository.loan_repository import LoanRepository
from backend.repository.book_repository import BookRepository


def return_book(
    book_id: int,
    student_id: int,
) -> bool:

    loan_repository = LoanRepository()
    book_repository = BookRepository()

    loan = loan_repository.get_by_ids(book_id, student_id)

    if not loan:
        return False

    loan.status = LoanStatusEnum.RETURNED
    loan_updated = loan_repository.update(loan)

    book = book_repository.get_by_id(book_id)
    if book:
        book.status = BookStatusEnum.ON_LIBRARY
        book_repository.update(book)

    return loan_updated
