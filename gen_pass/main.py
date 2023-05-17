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

    'a5':[ '_', '+', '=', '[', ']', '{', '}', '<', '>',','],

    'a6': ['U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'À', 'Â', 'Ã'],
    'a7': ['É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Ô', 'Ç'],

    'a8': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

    'a9': ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-'],

    'a10': ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
    
}
def random():
    timestamp = str(int(time.time_ns()) % 10000)
    return timestamp

def generatePassword(length):
    timestamp = random()
    password = ''
    c = 0

    i = 0
    while i < length:
        
        # gerar o index 
        char = timestamp[i % len(timestamp)]
        index = int(char)
        print ('a' + str(index))

        # seleciona a list
        list = data['a' + str(index)]

        # seleciona o caractere dentro da list
        if c > 10:
            c = 0
        element = list[len(timestamp) - c]

        # and de incrementarverifica se o ultimo elemento está sendo repetido 
        # se sim, procura novo elemento
        if len(password) > 0 and str(password[len(password) -1]) == element:
            password = password[:-1]
            length += 1
            # print('repetiu: ' + str(length))
            timestamp = random()

            # gerar o index 
            char = timestamp[i % len(timestamp)]
            index = int(char)
            # print ('a' + str(index))

            # seleciona a list
            list = data['a' + str(index)]

            # seleciona o caractere dentro da list
            if c > 10:
                c = 0
            element = list[len(timestamp) - c]

            timestamp = random()

        password += element

        # novo num aleatório baseado no tempo
        timestamp = random()
        c += 1
        i += 1
    return password

password = generatePassword(pass_length[0])
print(password)
