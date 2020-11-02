"""Friend data readers."""
import abc
import datetime
import typing

from birthday_greetings import Friend


class Reader(abc.ABC):
    """A reader that can get friend data."""

    @abc.abstractmethod
    def read_all(self) -> typing.Iterable[Friend]:
        """Read the data of all friends."""
        ...  # pragma: no cover

    def read_todays_birthdays(self, today: typing.Union[datetime.date, datetime.datetime]) -> typing.Iterable[Friend]:
        """Read data of friends who have birthdays today."""
        return (f for f in self.read_all() if f.is_birthday(today))
