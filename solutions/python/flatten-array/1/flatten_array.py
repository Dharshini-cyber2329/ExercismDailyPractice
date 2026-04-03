def flatten(iterable):
    result = []
    
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            result.extend(flatten(item))  # recursion
        else:
            result.append(item)
    
    return result