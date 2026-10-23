from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


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


def test_discount_100_nonprofit_false():
    assert get_event_discount(100, False) == 0.05


def test_nonprofit_status_changes_discount():
    assert get_event_discount(100, True) != get_event_discount(100, False)


def test_service_fee_at_500():
    assert round(calculate_event_total(25.00, 20), 2) == 575.00


def test_no_service_fee_over_500():
    assert round(calculate_event_total(25.05, 20), 2) == 501.00


def test_event_total_with_discount():
    assert round(calculate_event_total(22.00, 40), 2) == 836.00


def test_no_signoff_at_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_over_2500():
    assert needs_signoff(2500.01) is True


def test_no_second_chef_at_80_guests():
    assert needs_second_chef(80, 1000.00) is False


def test_no_second_chef_at_81_guests():
    assert needs_second_chef(81, 1000.00) is True


def test_no_second_chef_under_3000():
    assert needs_second_chef(48, 2999.99) is False


def test_no_second_chef_at_3000():
    assert needs_second_chef(48, 3000.00) is True


def test_total_booked_multiple_events():
    events = [
        {"client": "Client 1", "guest_price": 30.00, "guests": 12, "nonprofit": False},
        {"client": "Client 2", "guest_price": 35.00, "guests": 18, "nonprofit": False},
    ]
    assert round(total_booked(events), 2) == 1065.00


def test_total_booked_single_event():
    events = [
        {"client": "Client 1", "guest_price": 30.00, "guests": 15, "nonprofit": False}
    ]
    assert round(total_booked(events), 2) == 525.00


def test_largest_event_returns_largest_client():
    events = [
        {
            "client": "Small Event",
            "guest_price": 20.00,
            "guests": 10,
            "nonprofit": False,
        },
        {
            "client": "Large Event",
            "guest_price": 40.00,
            "guests": 50,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Large Event"


def test_largest_event_tie_returns_first_booked():
    events = [
        {
            "client": "First Client",
            "guest_price": 15.00,
            "guests": 12,
            "nonprofit": False,
        },
        {
            "client": "Second Client",
            "guest_price": 15.00,
            "guests": 12,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "First Client"


def test_largest_event_no_reservations():
    assert largest_event([]) == ""


def test_format_event_line_no_flags():
    result = format_event_line("Finch Law", 400.00, False, False)
    assert result == "Finch Law: $400.00 | Manager Sign-off: No | Second Chef: No"


def test_format_event_line_yes_flags():
    result = format_event_line("Hilltop Gym", 3000.00, True, True)
    assert result == "Hilltop Gym: $3000.00 | Manager Sign-off: Yes | Second Chef: Yes"


def test_format_event_line_two_decimals():
    result = format_event_line("Test Client", 100, False, False)
    assert "$100.00" in result
