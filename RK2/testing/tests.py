from io import StringIO
import unittest
from unittest.mock import patch, mock_open
import main


class TestProgram(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_filter_books_ending_with_ce(self):
        expected_result = [('Pride and Prejudice', 'University Library'), ('The Little Prince', 'University Library'), ('War and Peace', 'School Library')]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(str(book) in actual_output for book in expected_result))

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_average_year_by_lib(self):
        expected_result = [('School Library', 1869), ('University Library', 1878), ('City Public Library', 1940), ('Central Library', 1945), ('Community Library', 1945)]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(str(year) in actual_output for year in expected_result))

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_filter_libs_starting_with_c(self):
        expected_result = {'Central Library': ['To Kill a Mockingbird', 'The Great Gatsby', 'The Catcher in the Rye'], 'City Public Library': ['1984', 'Brave New World'], 'Community Library': ['The Lord of the Rings', 'The Hobbit']}
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(Lib in actual_output for Lib in expected_result.keys()))
            self.assertTrue(all(all(Book in actual_output for Book in Books) for Lib, Books in expected_result.items()))

if __name__ == '__main__':
    unittest.main()
