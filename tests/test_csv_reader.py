import datetime

"""Test the CSV reader."""
import operator
import pathlib
import unittest

from birthday_greetings import Friend
from birthday_greetings.reader.csv_reader import CSVReader
from tests import DATA_PATH, SAMPLE_FRIENDS


class TestCSVReader(unittest.TestCase):
    """Test the CSV reader."""

    def test_basic_data(self):
        """Test reading basic data."""
        reader = CSVReader(DATA_PATH / "sample-tests.csv")
        data = list(reader.read_all())
        data.sort(key=operator.attrgetter("email"))
        self.assertEqual(len(data), 2)
        self.assertEqual(data, SAMPLE_FRIENDS)

    def test_read_todays_birthdays(self):
        """Test reading today’s birthdays."""
        reader = CSVReader(DATA_PATH / "sample-tests.csv")
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
        reader = CSVReader(DATA_PATH / "sample-tests-invalid-date.csv")
        with self.assertRaises(Exception):
            data = list(reader.read_all())

    def test_invalid_fields(self):
        """Test reading file with invalid fields fails."""
        reader = CSVReader(DATA_PATH / "sample-tests-invalid-fields.csv")
        with self.assertRaises(Exception):
            data = list(reader.read_all())
