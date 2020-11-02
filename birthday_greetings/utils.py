"""Utilities for birthday_greetings."""

import datetime
import json
import typing

from birthday_greetings.reader import Reader
from birthday_greetings.sender import Sender


def parse_date(date_str: str) -> datetime.date:
    """Parse a date in Y/m/d format."""
    return datetime.datetime.strptime(date_str, "%Y/%m/%d").date()


def parse_extra_data(
    extra_data: typing.Optional[str],
) -> typing.Mapping[str, typing.Any]:
    """Parse extra data (JSON)."""
    if extra_data:
        return typing.cast(typing.Mapping[str, typing.Any], json.loads(extra_data))
    return {}


def send_messages(date: typing.Union[datetime.date, datetime.date], reader: Reader, sender: Sender) -> int:
    """Send messages to friends whose birthdays are on the given date."""
    friends_with_birthdays = reader.read_todays_birthdays(date)
    return sender.send_many(friends_with_birthdays)
