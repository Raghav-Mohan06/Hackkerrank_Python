def print_formatted(number):
    pad = number.bit_length()
    for i in range(1,number+1):
        print(str(i).rjust(pad),oct(i).split("o")[1].rjust(pad),hex(i).split("x")[1].upper().rjust(pad),bin(i).split("b")[1].rjust(pad))


