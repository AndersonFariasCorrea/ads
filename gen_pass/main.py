import library
import time

string_number = str(time.time())

length = library.parse_string_to_int(input("informe o tamanho da senha:\t"))

# Find the index of the decimal point
decimal_index = string_number.index('.')

# Extract the substring after the decimal point
numbers_after_decimal = string_number[decimal_index + 1:]

while length[1] is False and length[0] is not None and length[0] > 0:
    a = 0
