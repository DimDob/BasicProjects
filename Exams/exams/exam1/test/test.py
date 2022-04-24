import unittest
from project.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library('library1')

    def test_init(self):
        library = Library('library1')
        self.assertEqual(library.name, 'library1')
        self.assertEqual(library.books_by_authors, {})
        self.assertEqual(library.readers, {})

    def test_name_if_set_properly(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(ex.exception))


    def test_add_book_if_author_not_in_books_by_authors(self):
        self.assertEqual(True, 'author1' not in self.library.books_by_authors)
        self.library.add_book('author1', 'book1')
        self.assertEqual(self.library.books_by_authors['author1'], ['book1'])

    def test_add_book_if_title_not_in_books_by_author(self):
        self.library.books_by_authors['author1'] = ['book1']
        self.assertEqual(True, 'book2' not in self.library.books_by_authors)
        self.library.add_book('author1', 'book2')
        self.assertEqual(self.library.books_by_authors['author1'], ['book1', 'book2'])

    def test_add_reader_if_name_not_in_readers(self):
        self.assertEqual(True, 'reader1' not in self.library.readers)
        self.library.add_reader('reader1')
        self.assertEqual(self.library.readers['reader1'], [])

    def test_add_reader_if_name_is_in_readers(self):
        self.library.readers['reader1'] = []
        result = self.library.add_reader('reader1')
        expected = f"reader1 is already registered in the library1 library."
        self.assertEqual(result, expected)


    def test_rent_book_if_reader_name_not_in_readers(self):
        result = self.library.rent_book('reader1', 'author1', 'book1')
        expected = f"reader1 is not registered in the library1 Library."
        self.assertEqual(result, expected)

    def test_rent_book_if_author_not_in_books_by_authors(self):
        self.library.readers['reader1'] = []
        result = self.library.rent_book('reader1', 'author1', 'book1')
        expected = f"library1 Library does not have any author1's books."
        self.assertEqual(result, expected)

    def test_rent_book_if_title_does_not_exist(self):
        self.library.readers['reader1'] = []
        self.library.books_by_authors['author1'] = []
        result = self.library.rent_book('reader1', 'author1', 'book1')
        expected = f"""library1 Library does not have author1's "book1"."""
        self.assertEqual(result, expected)

    def test_rent_book_if_all_are_implemented(self):
        self.library.readers['reader1'] = []
        self.library.books_by_authors['author1'] = ['book1']

        self.library.rent_book('reader1', 'author1', 'book1')
        self.assertEqual(self.library.readers['reader1'], [{'author1':'book1'}])
        self.assertEqual(self.library.books_by_authors['author1'], [])