import library
import time

pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

while pass_length[1] is False:
    pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

data = {
    'a0': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    'a1': ['k', 'l', 'm', 'n', 'y', 'z', 'á', 'à', 'â', 'ã'],
    'a2': ['é', 'è', 'ê', 'í', 'o', 'p', 'q', 'r', 's', 't'],
    'a3': ['u', 'v', 'w', 'x', 'ì', 'î', 'ó', 'ò', 'ô', 'ç'],
    
    'a4': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'a5': ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    'a6': ['U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'À', 'Â', 'Ã'],
    'a7': ['É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Ô', 'Ç'],

    'a8': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

    'a9': ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-'],
    'a10':[ '_', '+', '=', '[', ']', '{', '}', '<', '>',','],
}

def generatePassword(length):
    timestamp = str(int(time.time()))
    password = ''

    for i in range(length):
        char = timestamp[i % len(timestamp)]
        index = int(char)

        array = data['a' + str(index)]

        elementIndex = index % len(array)
        element = array[elementIndex]

        password += element

        timestamp = str(int(time.time()))

    return password

password = generatePassword(pass_length[0])
print(password)
