def single_char_xor(hex_string):
    # Converto a string hexadecimal para bytes
    bytes_codificados = bytearray.fromhex(hex_string)

    strings_decodificadas = []  # crio uma lista vazia para adicionar as strings decodificadas.

    # Faço XOR com todos os caracteres/chaves possiveis(Brute force).
    for key in range(256):
        bytes_decodificados = bytearray(b ^ key for b in bytes_codificados)
        string_decodificada = bytes_decodificados.decode('utf-8', errors='ignore')  #decodifica o array para uma string.
        strings_decodificadas.append(string_decodificada)

    #Agora que tenho todas as strings possiveis, tenho que achar um meio de selecionar a mais provavel de ser a real.
    # Para isso vamos utilizar um sistema de pontuaçao por frequencia da letra no dicionario Ingles.
    # Funçao que mede a pontuaçao pela frequencia de letras em Ingles da string decodificada.
    def score(string):
        score = 0
        # Utilizamos um dicionario que atribui pontos dependendo da letra e sua frequencia
        # (fonte:"A Statistical Analysis of Letter Frequency in the English Language" by Peter Norvig)
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

    # Encontramos a string com a maior pontuaçao pela tabela de frequencia.
    strings_decodificadas.sort(key=score, reverse=True) #sort reverso para que o maior esteja na primeira posicao

    return strings_decodificadas[0] #retorno a string que estiver na posicao 0 da lista(maior score).


hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
frase = single_char_xor(hex_string)
print(frase)
