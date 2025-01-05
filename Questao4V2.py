def single_char_xor(hex_string):
    # Converto a string hexadecimal para bytes
    bytes_codificados = bytearray.fromhex(hex_string)

    strings_decodificadas = []

    #  Tento fazer o XOR com cada chave possivel(brute force)
    for key in range(256):
        bytes_decodificados = bytearray(b ^ key for b in bytes_codificados)
        string_decodificada = bytes_decodificados.decode('utf-8', errors='ignore')
        strings_decodificadas.append(string_decodificada)

    return strings_decodificadas

def score(string):
    score = 0
    frequencias_letras = {
         'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
            'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
            'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
            'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
            'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
            'z': 0.00074, ' ': 0.19181
    }
    for char in string.lower():
        if char in frequencias_letras:
            score += frequencias_letras[char]
    return score

#  Abro o arquivo com a string de hexadecimais(a chamei de SH.txt)
with open("SH.txt", "r") as f:
    linhas = f.readlines()

# Decripito cada linha
linhas_decripitadas = []
for linha in linhas:
    linha_original = linha
    decriptado_linha_linha = single_char_xor(linha.strip())
    linhas_decripitadas += [[linha_original.strip(), string_decripitada] for string_decripitada in decriptado_linha_linha]

# Ordeno as linhas pela sua pontuação, 
linhas_decripitadas.sort(key=lambda x: score(x[1]), reverse=True)

# Printo a mensagem com a maior pontuação 
print("Mensagem original:", linhas_decripitadas[0][0])
print("Mensagem decripitada:", linhas_decripitadas[0][1])
