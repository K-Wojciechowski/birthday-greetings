"""A sender that uses print() for demonstration purposes and pretends to be sending text messages."""
import typing

from birthday_greetings import Friend
from birthday_greetings.sender import Sender


def get_phone(friend: Friend) -> str:
    """Get a friend’s phone number."""
    phone: typing.Optional[str] = friend.extra_data.get("phone")
    if not phone:
        raise ValueError("Cannot send SMS, phone number not in extra data!")
    return phone


class PrintSMSSender(Sender):
    """A sender that uses print() for demonstration purposes and pretends to be sending text messages."""

    def send_one(self, friend: Friend) -> None:
        """Send a message to one friend."""
        phone = get_phone(friend)
        self.send_sms(friend, phone, self.format_message(friend))

    def send_sms(self, friend: Friend, phone: str, message: str) -> None:  # pragma: no cover
        """Send a SMS to a friend with a given phone number."""
        print("--- message start ---")
        print(f"To: {friend.first_name} {friend.last_name} <{phone}>")
        print("Subject: Happy birthday!")
        print("")
        print(message)
        print("--- message end ---")
