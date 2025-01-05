def xor_hex(hex_string1, hex_string2):
    int1 = int(hex_string1, 16)   # Converto as strings hexadecimais para inteiros.
    int2 = int(hex_string2, 16)

    xor_int = int1 ^ int2     # XOR dos inteiros

    xor_hex_string = format(xor_int, 'x')   #Converto o inteiro XOR para uma string hexadecimal novamente

    return xor_hex_string
hex_string1=input() #string hexadecimal
hex_string2=input()
xor = xor_hex(hex_string1, hex_string2)
print(xor)