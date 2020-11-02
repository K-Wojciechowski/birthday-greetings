"""A sender that uses print() for demonstration purposes."""
from birthday_greetings import Friend
from birthday_greetings.sender import Sender


class PrintSender(Sender):
    """A sender that uses print() for demonstration purposes."""

    def send_one(self, friend: Friend) -> None:
        """Send a message to one friend."""
        self.send_email(friend, friend.email, self.format_message(friend))

    def send_email(self, friend: Friend, email: str, message: str) -> None:  # pragma: no cover
        """Send an e-mail message to a friend with a given address."""
        print("--- message start ---")
        print(f"To: {friend.first_name} {friend.last_name} <{email}>")
        print("Subject: Happy birthday!")
        print("")
        print(message)
        print("--- message end ---")
