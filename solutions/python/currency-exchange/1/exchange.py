"""
Functions for calculating steps in exchanging currency.
"""


def exchange_money(budget, exchange_rate):
    """Return exchanged value of foreign currency."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Return remaining money after exchange."""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Return total value of bills."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Return number of bills that can be obtained."""
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Return leftover amount after getting bills."""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Return maximum exchangeable value after fees."""

    # Apply spread (fee)
    rate_with_spread = exchange_rate * (1 + spread / 100)

    # Convert money
    exchanged = exchange_money(budget, rate_with_spread)

    # Get number of bills
    bills = get_number_of_bills(exchanged, denomination)

    # Return value of bills
    return get_value_of_bills(denomination, bills)
