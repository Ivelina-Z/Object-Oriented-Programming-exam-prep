from unittest import TestCase, main
from unit_testing_class_library.library import Library


class LibraryTest(TestCase):
    def setUp(self):
        self.library = Library('lib')

    def test_successful_initialization(self):
        self.assertEqual('lib', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_validation_when_invalid_name_value_error_expected(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        result = str(ve.exception)
        expected_result = 'Name cannot be empty string!'

        self.assertEqual(expected_result, result)

    def test_successful_name_validation_valid_name(self):
        self.library.name = 'Lib'
        self.assertEqual('Lib', self.library.name)

    def test_add_book_new_author_new_title(self):
        self.library.books_by_authors = {'author1': ['book1']}
        self.library.add_book('author2', 'book2')

        result = self.library.books_by_authors
        expected_result = {'author1': ['book1'], 'author2': ['book2']}

        self.assertEqual(expected_result, result)

    def test_add_book_new_title(self):
        self.library.books_by_authors = {'author1': ['book1']}
        self.library.add_book('author1', 'book2')

        result = self.library.books_by_authors
        expected_result = {'author1': ['book1', 'book2']}

        self.assertEqual(expected_result, result)

    def test_add_reader_new_reader(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}
        self.library.add_reader('reader2')

        result = self.library.readers
        expected_result = {'reader1': [{'author': 'title'}], 'reader2': []}

        self.assertEqual(expected_result, result)

    def test_add_reader_existing_reader(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}

        result = self.library.add_reader('reader1')
        expected_result = "reader1 is already registered in the lib library."

        self.assertEqual(expected_result, result)

    def test_rent_book_reader_not_in(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}

        result = self.library.rent_book('reader2', 'author1', 'book1')
        expected_result = 'reader2 is not registered in the lib Library.'

        self.assertEqual(expected_result, result)

    def test_rent_book_author_not_in(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}
        self.library.books_by_authors = {'author1': ['title1']}

        result = self.library.rent_book('reader1', 'author2', 'book1')
        expected_result = "lib Library does not have any author2's books."

        self.assertEqual(expected_result, result)

    def test_rent_book_title_not_in(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}
        self.library.books_by_authors = {'author1': ['title1']}

        result = self.library.rent_book('reader1', 'author1', 'book1')
        expected_result = """lib Library does not have author1's "book1"."""

        self.assertEqual(expected_result, result)

    def test_rent_book_successfully(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}
        self.library.books_by_authors = {'author1': ['title2']}

        self.library.rent_book('reader1', 'author1', 'title2')
        result = self.library.readers['reader1']
        expected_result = [{'author': 'title'}, {'author1': 'title2'}]
        self.assertEqual(expected_result, result)

    def test_delete_book_from_library_after_rented(self):
        self.library.readers = {'reader1': [{'author': 'title'}]}
        self.library.books_by_authors = {'author1': ['title1']}
        self.library.rent_book('reader1', 'author1', 'title1')
        result = self.library.books_by_authors['author1']
        expected_result = []
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
