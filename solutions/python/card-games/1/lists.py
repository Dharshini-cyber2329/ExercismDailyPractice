def get_rounds(number):
    # Current round and next two
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    # Join two lists
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    # Check if number is in list
    return number in rounds


def card_average(hand):
    # Average = sum / count
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    # True average
    avg = card_average(hand)

    # First + last average
    first_last_avg = (hand[0] + hand[-1]) / 2

    # Middle card
    mid = hand[len(hand) // 2]

    return avg == first_last_avg or avg == mid


def average_even_is_average_odd(hand):
    # Even index values
    even = hand[0::2]

    # Odd index values
    odd = hand[1::2]

    even_avg = sum(even) / len(even)
    odd_avg = sum(odd) / len(odd)

    return even_avg == odd_avg


def maybe_double_last(hand):
    # If last card is Jack (11), double it
    if hand[-1] == 11:
        hand[-1] *= 2

    return hand