"""Senders that can send messages to friends."""
import abc
import typing

from birthday_greetings import Friend


class Sender(abc.ABC):
    """A way to send messages to friends."""

    def format_message(self, friend: Friend) -> str:
        """Format a message to a friend."""
        return f"Happy birthday, dear {friend.first_name}!"

    @abc.abstractmethod
    def send_one(self, friend: Friend) -> None:
        """Send a message to one friend."""
        ...  # pragma: no cover

    def send_many(self, friends: typing.Iterable[Friend]) -> int:
        """Send messages to multiple friends."""
        sent_messages = 0
        for friend in friends:
            self.send_one(friend)
            sent_messages += 1
        return sent_messages
