"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    """Determine the scoring value of a card."""

    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value."""

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the best value for an ace."""

    total = 0

    for card in [card_one, card_two]:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
        else:
            total += int(card)

    # Check if ace should be 1 or 11
    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Check if hand is blackjack."""

    cards = [card_one, card_two]

    if "A" in cards:
        other = card_two if card_one == "A" else card_one
        return value_of_card(other) == 10

    return False


def can_split_pairs(card_one, card_two):
    """Check if cards can be split."""

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Check if player can double down."""

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in [9, 10, 11]
