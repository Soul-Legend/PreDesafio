def repeating_key_xor(texto, key):
    # Calculo o tamanho da chave
    key_len = len(key)
    
    # Converto o texto para um objeto de bytearray
    bytes_texto = bytearray(texto, "utf-8") 
    
    #  Inicializo o bytearray para armazenar a mensagem encripitada
    bytes_encriptados = bytearray()
    
    #  Itero por cada caracter do texto
    for i, b in enumerate(bytes_texto):
        #  faço o XOR de cada caracter com a parte da chave correspondente
        bytes_encriptados.append(b ^ ord(key[i % key_len]))
    
    # Retorno a mensagem encripitada como uma string hexadecimal
    return bytes_encriptados.hex()

texto = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

texto_encripitado = repeating_key_xor(texto, key)
print(texto_encripitado)
