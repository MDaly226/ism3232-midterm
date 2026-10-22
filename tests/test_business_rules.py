from business_rules import calculate_food_cost, get_event_discount


def test_calculate_food_cost():
    assert calculate_food_cost(20.00, 10) == 200.00


def test_discount_24_guests():
    assert get_event_discount(24) == 0.00


def test_discount_25_guests():
    assert get_event_discount(25) == 0.05


def test_discount_99_guests():
    assert get_event_discount(99) == 0.05


def test_discount_100_nonprofit_guests():
    assert get_event_discount(100, True) == 0.12


def test_discount_100_nonprofit_guests():
    assert get_event_discount(100, False) == 0.05


def test_nonprofit_status_changes_discount():
    assert get_event_discount(100, True) != get_event_discount(100, False)
