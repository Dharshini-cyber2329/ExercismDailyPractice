"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate seat letters A–D repeatedly."""
    letters = ["A", "B", "C", "D"]

    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate seat numbers like 1A, 1B, skipping row 13."""
    row = 1
    generated = 0

    while generated < number:
        if row == 13:  # skip row 13
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:
            if generated >= number:
                break
            yield f"{row}{letter}"
            generated += 1

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers."""
    seats = generate_seats(len(passengers))
    assignments = {}

    for passenger in passengers:
        assignments[passenger] = next(seats)

    return assignments


def generate_codes(seat_numbers, flight_id):
    """Generate 12-character ticket codes."""
    for seat in seat_numbers:
        code = seat + flight_id
        yield code.ljust(12, "0")