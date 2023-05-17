def parse_string_to_int(string):
    try:
        number = int(string)
        return number, True
    except ValueError:
        return None, False