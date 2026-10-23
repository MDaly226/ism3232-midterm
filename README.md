# ISM3232 Midterm: Harvest Table Catering

- Michael Daly
- Version BETA
- 10/23/2026

## What This Program Does:
This program calculates the total prices of catering events for Harvest Table Catering. It totals prices based off of applicable discounts based off guest totals and nonprofit status, service fees, manager signoff rules, and additional chef requirements. It prints out a report for the company showing them each event and a summary of all booked events.

## Business Rules:
1. Food cost is the price per guest multiplied by the number of guests.
2. Events with fewer than 25 guests recieve no discounts, while events with 25 or more guests recieve a discount of 5%.
3. Events with 100 or more guests recieve a 12% discount ONLY if they are also registered nonprofits. Any other event with 100 or more guests only recieve the 5% discount.
4. A $75 service fee is added when the discounted event cost is $500 or lower, even if there is no discount.
5. Any event with a total cost of over $2,500 requires an manager to sign-off on the event.
6. A second chef is required at any event that has more than 80 guests or any event with a total cost of $3,000 or more.

## How to Run:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to Test:
ruff format --check .
ruff check .
pytest -v
(There are 24 tests)

## Files in This Repository:
business_rules.py - These are the 8 business rule functions.
main.py - This runs the event report and prints the results.
commands.md - Contains the terminal commands and outputs used to build and setup the project.
README.md - Explains what the project does, how to run and test it, and the files cin the repository.
requirements.txt - Contains a list of the required python packages to use the program.
.gitignore - Stops particular local environment files from being committed.
tests/__init__.py - States the tests folder as a python package.
tests/test_business_rules.py - Contains the pytest tests for the business rule functions.

## AI Use Statement
I did not use AI on this exam project. *Thank you for letting us use the course site, I'd have been lost without it.