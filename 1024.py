N = int(input())
for i in range(0, N):
    texto = input()
    tamanho = len(texto) - int(len(texto)/2)
    textoCodificado = ''
    contador = 0

    for caractere in texto:
        if (caractere.isalpha()):
            if(contador<tamanho):
                textoCodificado += chr(ord(caractere)+2)
            else:
                textoCodificado += chr(ord(caractere)+3)
        else:
            if(contador<tamanho):
                textoCodificado += chr(ord(caractere)-1)
            else:
                textoCodificado += caractere
        contador += 1


    textoCodificado = textoCodificado[::-1]
    print(textoCodificado)
