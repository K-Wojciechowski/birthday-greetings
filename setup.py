#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="birthday_greetings",
    version="0.1.0",
    description="A simple app to send e-mail greetings to friends.",
    author="Krzysztof Wojciechowski",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "birthday_greetings = birthday_greetings.cli:main",
        ]
    },
)
