import unittest
from bible_summary.summary import BibleSummary

class TestBibleSummary(unittest.TestCase):

    def setUp(self):
        self.bible_summary = BibleSummary(data_dir="bible_summary/data")

    def test_get_books(self):
        books = self.bible_summary.get_books()
        self.assertIn("1 Chronicles", books)

    def test_get_summary(self):
        summary = self.bible_summary.get_summary("1 Chronicles", "1")
        self.assertTrue(summary.startswith("Adam, Seth, Noah"))

    def test_get_chapters(self):
        chapters = self.bible_summary.get_chapters("1 Chronicles")
        self.assertIn("1", chapters)

if __name__ == '__main__':
    unittest.main()
