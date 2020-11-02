"""Tests for birthday_greetings."""
import datetime
import pathlib

from birthday_greetings import Friend

DATA_PATH = pathlib.Path(__file__).parent / "data"
SAMPLE_FRIENDS = [
    Friend("Doe", "John", datetime.date(1982, 10, 8), "john.doe@foobar.com"),
    Friend(
        "Ann",
        "Mary",
        datetime.date(1975, 9, 11),
        "mary.ann@foobar.com",
        {"phone": "123456789"},
    ),
]
SAMPLE_MESSAGES = [
    "Happy birthday, dear John!",
    "Happy birthday, dear Mary!",
]
