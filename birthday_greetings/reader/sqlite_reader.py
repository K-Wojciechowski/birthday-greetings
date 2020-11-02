"""A friend reader that uses a SQLite database."""
import datetime
import sqlite3
import typing

from birthday_greetings import Friend, utils
from birthday_greetings.reader import Reader


class SQLiteReader(Reader):
    """A friend reader that uses a SQLite database as input."""

    conn: sqlite3.Connection

    def __init__(self, conn_or_file_name: typing.Union[str, sqlite3.Connection]):
        """Initialize a SQLite reader."""
        if isinstance(conn_or_file_name, str):
            self.conn: sqlite3.Connection = sqlite3.connect(conn_or_file_name)
        else:
            self.conn = conn_or_file_name

    def read_all(self) -> typing.Iterable[Friend]:
        """Read the data of all friends."""
        cur: sqlite3.Cursor = self.conn.cursor()
        cur.execute("SELECT last_name, first_name, date_of_birth, email, extra_data FROM friend")
        for row in cur:
            yield _get_friend_from_row(row)
        cur.close()

    def read_todays_birthdays(self, today: typing.Union[datetime.date, datetime.datetime]) -> typing.Iterable[Friend]:
        """Read data of friends who have birthdays today."""
        dob_pattern = today.strftime("____/%m/%d")
        today_formatted = today.strftime("%Y/%m/%d")  # Don’t send greetings before birthday
        cur: sqlite3.Cursor = self.conn.cursor()
        cur.execute(
            "SELECT last_name, first_name, date_of_birth, email, extra_data FROM friend "
            "WHERE date_of_birth LIKE ? AND date_of_birth <= ?",
            (dob_pattern, today_formatted),
        )
        for row in cur:
            yield _get_friend_from_row(row)
        cur.close()

    def close_conn(self) -> None:
        """Close the database connection."""
        self.conn.close()


def _get_friend_from_row(row: typing.Tuple[str, str, str, str, str]) -> Friend:
    """Get friend data from a database row."""
    last_name, first_name, date_of_birth, email, extra_data = row
    return Friend(
        last_name=last_name,
        first_name=first_name,
        date_of_birth=utils.parse_date(date_of_birth),
        email=email,
        extra_data=utils.parse_extra_data(extra_data),
    )
