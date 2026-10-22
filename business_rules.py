# business_rules.py

NO_DISCOUNT = 0.00
REGULAR_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12

REGULAR_DISCOUNT_MIN_GUESTS = 25
NONPROFIT_DISCOUNT_MIN_GUESTS = 100

SERVICE_FEE = 75.00
SERVICE_FEE_LIMIT = 500

SIGNOFF_LIMIT = 2500.00

SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Returns the food cost before discounts are applied."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Returns the discount rate for an event."""
    if guests >= NONPROFIT_DISCOUNT_MIN_GUESTS:
        if nonprofit:
            return NONPROFIT_DISCOUNT
        return REGULAR_DISCOUNT

    if guests >= REGULAR_DISCOUNT_MIN_GUESTS:
        return REGULAR_DISCOUNT

    return NO_DISCOUNT
