"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""
    
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""
    
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""
    
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = rui_record[1]
    
    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""
    
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],   # treasure name
            azara_record[1],   # azara coordinate string
            rui_record[0],     # location name
            rui_record[1],     # rui coordinate tuple
            rui_record[2]      # quadrant
        )
    else:
        return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    The return statement should be a multi-lined string with items separated by newlines.
    """

    cleaned_records = []

    for record in combined_record_group:
        treasure = record[0]
        location = record[2]
        coordinate_tuple = record[3]
        quadrant = record[4]

        cleaned_records.append(
            str((treasure, location, coordinate_tuple, quadrant))
        )

    return "\n".join(cleaned_records) + "\n"