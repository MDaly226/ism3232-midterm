# Terminal Record: Harvest Table Catering

## 1. Building the project

## I used mkdir ism3232-midterm to create the folder, then I connected it to github with git init, git remote add origin https://github.com/MDaly226/ism3232-midterm.git, git branch -M main. I checked to make sure I was linked with git remote -v. Then I created the files with touch business_rules.py, touch main.py, touch commands.md, touch README.md, touch requirements.txt, touch .gitignore, mkdir tests, then in tests, I used touch (underscore underscore)init(underscore underscore).py, and touch test_business_rules.py. I tried to use && during my initial create but I must have done something wrong as only a few were created so I decided to just do everything individually to make sure they were all there. I just realized I forgot freeze and pytest ruff So I have added them by using "pip install pytest ruff && pip freeze > requirements.txt"

## 2. The Virtual Environment

## which python3 Produces: /home/MDaly/ism3232/ism3232_midterm/.venv/bin/python3       the .venv is what shows that the virtual environment is active in the path.

## 3. The Project Structure

## tree -L 2 produces: 
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

## __pycache__ folder is on my pc but shouldnt be in the github repository because it should be ignored by my .gitignore.

## 4. Every Function and Test

## tests/test_business_rules.py
13:def test_calculate_food_cost():
17:def test_discount_24_guests():
21:def test_discount_25_guests():
25:def test_discount_99_guests():
29:def test_discount_100_nonprofit_guests():
33:def test_discount_100_nonprofit_false():
37:def test_nonprofit_status_changes_discount():
41:def test_service_fee_at_500():
45:def test_no_service_fee_over_500():
49:def test_event_total_with_discount():
53:def test_no_signoff_at_2500():
57:def test_signoff_over_2500():
61:def test_no_second_chef_at_80_guests():
65:def test_no_second_chef_at_81_guests():
69:def test_no_second_chef_under_3000():
73:def test_no_second_chef_at_3000():
77:def test_total_booked_multiple_events():
85:def test_total_booked_single_event():
92:def test_largest_event_returns_largest_client():
110:def test_largest_event_tie_returns_first_booked():
128:def test_largest_event_no_reservations():
132:def test_format_event_line_no_flags():
137:def test_format_event_line_yes_flags():
142:def test_format_event_line_two_decimals():

business_rules.py
19:def calculate_food_cost(guest_price: float, guests: int) -> float:
24:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
37:def calculate_event_total(
51:def needs_signoff(total: float) -> bool:
56:def needs_second_chef(guests: int, total: float) -> bool:
61:def total_booked(events: list) -> float:
76:def largest_event(events: list) -> str:
98:def format_event_line(

## business_rules.py defines 8 functions, and tests/test_business_rules.py defines 24 tests that I created for those functions.

## 5. Which Files Print

## main.py is the only file that prints. business_rules.py doesnt print, it only returns values.

## 6. The Commit History

## git log --oneline produces:
85f6325 (HEAD -> main, origin/main) Added the Harvest Table Catering event report
adea8d8 Added formatting for event report with tests
402f348 added booked total and largest event loops with tests.
af48385 Added signoff and second chef rules and tests.
5a11cc3 Added calculation for event total, tests for fees, and also updated def. for discount_100_nonprofit_false.
37bb583 Added food cost and discount rules, tests for food cost and discounts, and updated gitignore
456699e Part 1 - setup

## So far up to this point there have been 7 commits.