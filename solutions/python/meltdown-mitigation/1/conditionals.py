"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""

    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""

    value = temperature * neutrons_produced_per_second

    lower_bound = threshold * 0.9
    upper_bound = threshold * 1.1

    if value < lower_bound:
        return "LOW"
    elif lower_bound <= value <= upper_bound:
        return "NORMAL"
    else:
        return "DANGER"
