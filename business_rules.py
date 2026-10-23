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


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Calculates the final total for a particular event."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)

    if discounted_cost <= SERVICE_FEE_LIMIT:
        return discounted_cost + SERVICE_FEE

    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Returns whether an event needs a manager to sign-off before proceeding."""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Returns if the event will need a second chef based on guest total or cost total."""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Returns the total value of all booked events"""
    total = 0.00

    for event in events:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )
        total += event_total

    return total


def largest_event(events: list) -> str:
    """Returns the client with the largest event total price."""
    if not events:
        return ""

    largest_client = ""
    largest_total = -1.0

    for event in events:
        event_total = calculate_event_total(
            event["guest_price"],
            event["guests"],
            event["nonprofit"],
        )

        if event_total > largest_total:
            largest_total = event_total
            largest_client = event["client"]

    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Formats one event for reports"""
    signoff_text = "Yes" if signoff else "No"
    chef_text = "Yes" if second_chef else "No"

    return (
        f"{client}: ${total:.2f} | "
        f"Manager Sign-off: {signoff_text} | "
        f"Second Chef: {chef_text}"
    )
