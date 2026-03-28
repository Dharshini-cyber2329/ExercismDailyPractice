def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6,
        "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }

    # 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        value = (color_values[colors[0]] * 10 +
                 color_values[colors[1]])
        multiplier = 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]

    # 5-band resistor
    elif len(colors) == 5:
        value = (color_values[colors[0]] * 100 +
                 color_values[colors[1]] * 10 +
                 color_values[colors[2]])
        multiplier = 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]

    total = value * multiplier

    # Convert units properly (KEEP DECIMALS)
    if total >= 1_000_000:
        total = total / 1_000_000
        unit = "megaohms"
    elif total >= 1_000:
        total = total / 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    # Format number cleanly
    total = round(total, 2)
    if isinstance(total, float) and total.is_integer():
        total = int(total)

    return f"{total} {unit} {tolerance}"