"""A friend reader that uses CSV files."""
import csv
import os
import typing

from birthday_greetings import Friend, utils
from birthday_greetings.reader import Reader


class SpacedDialect(csv.Dialect):
    """A CSV dialect that supports spaces after fields."""

    delimiter = ","
    doublequote = False
    escapechar = "\\"
    lineterminator = "\r\n"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = True
    strict = False


class CSVReader(Reader):
    """A friend reader that uses CSV files as input."""

    file_name: typing.Union[str, os.PathLike[typing.Any]]

    def __init__(self, file_name: typing.Union[str, os.PathLike[typing.Any]]):
        """Initialize a CSV reader."""
        self.file_name = file_name

    def read_all(self) -> typing.Iterable[Friend]:
        """Read the data of all friends."""
        with open(self.file_name, newline="") as fh:
            for data in csv.DictReader(fh, dialect=SpacedDialect):
                yield Friend(
                    last_name=data["last_name"],
                    first_name=data["first_name"],
                    date_of_birth=utils.parse_date(data["date_of_birth"]),
                    email=data["email"],
                    extra_data=utils.parse_extra_data(data.get("extra_data")),
                )
