.PHONY: style types tests tests_nocov all

all: style types tests

style:
	isort -l 120 .
	black -l 120 .

types:
	python -m mypy --strict -p birthday_greetings

tests:
	python -m coverage run -m unittest
	python -m coverage html

tests_nocov:
	python -m unittest
