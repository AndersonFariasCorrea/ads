import library
import time

pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

while pass_length[1] is False:
    pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

data = {
    'a1': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'ç'],
    'a2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'À', 'Â', 'Ã', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Ô', 'Õ', 'Ú', 'Ù', 'Û', 'Ç'],
    'a3': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'a4': ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', '/', '<', '>', ',', '.', ';', ':', '?']
}

def generatePassword(length):
    timestamp = str(int(time.time() * 1000))
    password = ''

    for i in range(length):
        char = timestamp[i % len(timestamp)]
        index = int(char)

        array = data['a' + str(index % 4 + 1)]

        elementIndex = index % len(array)
        element = array[elementIndex]

        password += element

    return password

password = generatePassword(pass_length[0])
print(password)
