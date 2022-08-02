def inverterPalavra(palavra='python'):
    fragmento = []
    for letra in palavra:
        fragmento.append(letra)

    print(fragmento)

    for i in range(len(fragmento) -1, -1, -1):
        print(fragmento[i], end=' ')

inverterPalavra('Desenvolvedor')