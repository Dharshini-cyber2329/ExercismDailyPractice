"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param wagons: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    engine, caboose, *middle = each_wagons_id
    first, *rest = middle
    return [first, *missing_wagons, *rest, engine, caboose]


def add_missing_stops(route, **stops):
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]