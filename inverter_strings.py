def inverterPalavra(palavra='python'):
    fragmento = []
    for letra in palavra:
        fragmento.append(letra)

    invertido = ''

    for i in range(len(fragmento) -1, -1, -1):
        invertido += fragmento[i]
    
    return invertido 


print(inverterPalavra('Desenvolvedor'))
