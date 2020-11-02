"""Birthday greetings project."""
import dataclasses
import datetime
import typing


@dataclasses.dataclass
class Friend:
    """A friend to which birthday greetings can be sent."""

    last_name: str
    first_name: str
    date_of_birth: typing.Union[datetime.date, datetime.datetime]
    email: str
    extra_data: typing.Mapping[str, typing.Any] = dataclasses.field(default_factory=dict)

    def is_birthday(self, today: typing.Union[datetime.date, datetime.datetime]) -> bool:
        """Check if the given date is the friend’s birthday."""
        return (
            self.date_of_birth.month == today.month
            and self.date_of_birth.day == today.day
            and self.date_of_birth.year <= today.year
        )
