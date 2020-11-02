"""Test the list reader."""
import datetime
import unittest

from birthday_greetings.reader.list_reader import ListReader
from tests import SAMPLE_FRIENDS


class TestListReader(unittest.TestCase):
    """Test the list reader."""

    def test_basic_data(self):
        """Test reading basic data."""
        reader = ListReader(SAMPLE_FRIENDS)
        self.assertEqual(SAMPLE_FRIENDS, list(reader.read_all()))

    def test_read_todays_birthdays(self):
        """Test reading today’s birthdays."""
        reader = ListReader(SAMPLE_FRIENDS)
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
