import library
import time



pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

string_number = str(time.time())

# Find the index of the decimal point
decimal_index = string_number.index('.')

# Extract the substring after the decimal point
numbers_after_decimal = string_number[decimal_index + 1:]

while pass_length[1] is False and pass_length[0] is not None:
    if  pass_length[0] > 6 and pass_length[0] < 16:
        pass_length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))
