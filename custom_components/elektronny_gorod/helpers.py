import json

def is_json(value: str):
    try:
        json.loads(value)
    except ValueError as e:
        return False
    return True

def contains(list, condition):
    return any(condition(item) for item in list)

def find(list, condition):
    return next(
        (item for item in list if condition(item)),
        None
    )