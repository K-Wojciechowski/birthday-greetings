"""A friend reader that uses a list."""
import typing

from birthday_greetings import Friend
from birthday_greetings.reader import Reader


class ListReader(Reader):
    """A friend reader that uses a list as input."""

    data: typing.List[Friend]

    def __init__(self, data: typing.List[Friend]):
        """Initialize a list reader."""
        self.data = data

    def read_all(self) -> typing.Iterable[Friend]:
        """Read the data of all friends."""
        return self.data
