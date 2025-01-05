import base64 #Biblioteca padrao de Python

def hex_para_64(string_hex):
    bytes_hex = bytes.fromhex(string_hex)   # Converto a string hexadecimal para bytes
    base64_bytes = base64.b64encode(bytes_hex)  # Codifico bytes para base 64
    string_base64 = base64_bytes.decode("utf-8")  # Decodifico os bytes de  base 64 para uma string
    return string_base64
string_hex= input()
base64 = hex_para_64(string_hex) #Chamo a funçao para a converçao
print(base64)