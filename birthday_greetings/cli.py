"""CLI for birthday_greetings."""
import datetime
import sys
import traceback

from birthday_greetings import utils
from birthday_greetings.settings import READER, SENDER


def main() -> int:
    """Run the main CLI routine."""
    print("Birthday Greetings")
    print("==================")
    print("Enter the current date in YYYY/MM/DD format, leave blank for today, or type 'q' to exit.")
    while True:
        try:
            date_input = input("Date: ").strip()
        except KeyboardInterrupt:
            print()
            return 0

        if date_input == "q":
            break

        if date_input:
            date = utils.parse_date(date_input)
        else:
            date = datetime.date.today()

        try:
            sent = utils.send_messages(date, READER, SENDER)
            print(f"Sent {sent} messages.")
        except Exception:
            print("ERROR: failed to send messages!")
            traceback.print_exc()

    return 0


if __name__ == "__main__":
    sys.exit(main())
