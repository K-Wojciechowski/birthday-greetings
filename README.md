Birthday Greetings
==================

A simple app to send birthday greetings to people on their birthdays.

Features
--------

* Support for CSV and SQLite data sources
* Support for multiple ways of sending messages (currently simulates e-mail and SMS)
* Extensibility — modular design

CLI usage
---------

1. Edit `birthday_greetings/settings.py` to choose your reader and sender backends.
2. If you intend to use the SQLite backend, create the database first: `sqlite3 db.sqlite3 < sample.sql`
3. Run `python -m birthday_greetings` to use the CLI.

You can install in a venv with `pip install -e .` if you want (it will create a `birthday_greetings` command).

Tests
-----

Run `python -m unittest` to run the test suite.

Dependencies
------------

Runtime: Python 3.7+ with no external dependencies (or 3.6 with a `dataclasses` backport)

Development (optional): black, isort (code style); mypy (type checking) coverage (code coverage). Run `make` to reformat code, check types and run tests with coverage.

License
-------

MIT License

Copyright (c) 2020 Krzysztof Wojciechowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
