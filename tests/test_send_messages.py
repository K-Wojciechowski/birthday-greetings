"""Test message sending."""
import datetime
import pathlib
import unittest
import unittest.mock

from birthday_greetings import Friend, utils
from birthday_greetings.reader.list_reader import ListReader
from birthday_greetings.sender.print_sender import PrintSender
from birthday_greetings.sender.print_sms_sender import PrintSMSSender
from tests import SAMPLE_FRIENDS, SAMPLE_MESSAGES


class TestSendMessages(unittest.TestCase):
    """Test message sending."""

    def test_email_sending(self):
        """Test sending e-mails."""
        reader = ListReader(SAMPLE_FRIENDS)
        sender = PrintSender()

        with unittest.mock.patch.object(PrintSender, "send_email") as send_email:
            utils.send_messages(datetime.date(2020, 11, 7), reader, sender)
            send_email.assert_not_called()

            utils.send_messages(datetime.date(2000, 9, 11), reader, sender)
            f, msg = SAMPLE_FRIENDS[1], SAMPLE_MESSAGES[1]
            send_email.assert_called_with(f, f.email, msg)

            utils.send_messages(datetime.date(2000, 10, 8), reader, sender)
            f, msg = SAMPLE_FRIENDS[0], SAMPLE_MESSAGES[0]
            send_email.assert_called_with(f, f.email, msg)

        with unittest.mock.patch.object(PrintSender, "send_email") as send_email:
            utils.send_messages(datetime.date(1900, 10, 8), reader, sender)
            send_email.assert_not_called()

    def test_sms_sending(self):
        """Test sending text messages."""
        reader = ListReader(SAMPLE_FRIENDS)
        sender = PrintSMSSender()

        with unittest.mock.patch.object(PrintSMSSender, "send_sms") as send_sms:
            utils.send_messages(datetime.date(2020, 11, 7), reader, sender)
            send_sms.assert_not_called()

            utils.send_messages(datetime.date(2000, 9, 11), reader, sender)
            f, msg = SAMPLE_FRIENDS[1], SAMPLE_MESSAGES[1]
            send_sms.assert_called_with(f, f.extra_data["phone"], msg)

        with unittest.mock.patch.object(PrintSMSSender, "send_sms") as send_sms:
            with self.assertRaises(Exception):
                utils.send_messages(datetime.date(2000, 10, 8), reader, sender)
            send_sms.assert_not_called()

        with unittest.mock.patch.object(PrintSender, "send_email") as send_email:
            utils.send_messages(datetime.date(1900, 9, 11), reader, sender)
            send_email.assert_not_called()
