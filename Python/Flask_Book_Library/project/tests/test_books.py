import pytest
from project.books.models import Book


def test_create_book():
    book = Book(
        name="Test Book",
        author="Tester",
        year_published=2020,
        book_type="fantasy",
        status="available"
    )

    assert book.name == "Test Book"
    assert book.author == "Tester"
    assert book.year_published == 2020
    assert book.book_type == "fantasy"
    assert book.status == "available"


def test_book_repr():
    book = Book("A", "B", 1999, "thriller")
    rep = repr(book)
    assert "Book(" in rep
    assert "Name: A" in rep
