"""Test the SQLite reader."""
import datetime
import operator
import pathlib
import sqlite3
import tempfile
import unittest

from birthday_greetings import Friend
from birthday_greetings.reader.sqlite_reader import SQLiteReader
from tests import DATA_PATH, SAMPLE_FRIENDS


class TestSQLiteReader(unittest.TestCase):
    """Test the SQLite reader."""

    def setUp(self):
        """Set up a test by loading test data."""
        sample_script = (DATA_PATH / "sample-tests.sql").read_text()
        self.reader_tempfile = tempfile.NamedTemporaryFile("w+b")
        tempfile_conn = sqlite3.connect(self.reader_tempfile.name)
        tempfile_conn.executescript(sample_script)
        self.reader_file = SQLiteReader(self.reader_tempfile.name)
        memory_conn = sqlite3.connect(":memory:")
        memory_conn.executescript(sample_script)
        self.reader_conn = SQLiteReader(memory_conn)
        self.readers = [self.reader_file, self.reader_conn]

    def tearDown(self):
        """Close connections and files."""
        for r in self.readers:
            r.close_conn()
        self.reader_tempfile.close()

    def test_basic_data(self):
        """Test reading basic data."""
        for reader in self.readers:
            data = list(reader.read_all())
            data.sort(key=operator.attrgetter("email"))
            self.assertEqual(len(data), 2)
            self.assertEqual(data, SAMPLE_FRIENDS)

    def test_read_todays_birthdays(self):
        """Test reading today’s birthdays."""
        for reader in self.readers:
            self.assertEqual(list(reader.read_todays_birthdays(datetime.date(2020, 11, 7))), [])
            self.assertEqual(
                list(reader.read_todays_birthdays(datetime.date(2020, 10, 8))),
                [SAMPLE_FRIENDS[0]],
            )
            self.assertEqual(
                list(reader.read_todays_birthdays(datetime.date(2000, 9, 11))),
                [SAMPLE_FRIENDS[1]],
            )
            self.assertEqual(list(reader.read_todays_birthdays(datetime.date(1900, 9, 11))), [])

    def test_invalid_date(self):
        """Test reading file with an invalid date fails."""
        sample_script = (DATA_PATH / "sample-tests-insert-invalid-date.sql").read_text()
        for reader in self.readers:
            reader.conn.executescript(sample_script)
            with self.assertRaises(Exception):
                data = list(reader.read_all())
