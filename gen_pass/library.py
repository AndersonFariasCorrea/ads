lowercase_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'ç')

uppercase_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'À', 'Â', 'Ã', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Ô', 'Õ', 'Ú', 'Ù', 'Û', 'Ç')

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

special_characters = ('!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', '/', '<', '>', ',', '.', ';', ':', '?')

def parse_string_to_int(string):
    try:
        result = None
        number = int(string)
        if number >= 6 and number <= 16:
            result = number, True
        else:
            result = None, False
        return result, 
    except ValueError:
        return None, False
