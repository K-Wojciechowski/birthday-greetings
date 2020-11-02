"""Settings for birthday_greetings."""
from birthday_greetings.reader import csv_reader
from birthday_greetings.sender import print_sender

# Which reader to use to get birthdays? (Pass an instance of a Reader subclass.)
# READER = csv_reader.CSVReader("sample.csv")
READER = csv_reader.CSVReader("sample-phone.csv")
# READER = sqlite_reader.SQLiteReader("db.sqlite3")
# READER = list_reader.ListReader([Friend(…)])

# Which sender to use to send messages? (Pass an instance of a Sender subclass.)
SENDER = print_sender.PrintSender()
# SENDER = print_sms_sender.PrintSMSSender()
