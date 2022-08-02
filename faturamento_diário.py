import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

def menorValor(dados):
    menor_valor = ''
    dia_menor_valor = ''
    for i in dados:
        if menor_valor == '' and i['valor'] != 0:
            menor_valor = i['valor']
            dia_menor_valor = i['dia']

        if menor_valor > i['valor'] and i['valor'] != 0.0:
            menor_valor = i['valor']
            dia_menor_valor = i['dia']

    print(f"O menor valor de faturamento foi de {menor_valor}, ocorreu no dia {dia_menor_valor}.")


def maiorValor(dados):
    maior_valor = ''
    dia_maior_valor = ''
    for i in dados:
        if maior_valor == '' and i['valor'] != 0:
            maior_valor = i['valor']
            dia_maior_valor = i['dia']

        if maior_valor < i['valor']:
            maior_valor = i['valor']
            dia_maior_valor = i['dia']

    print(f"O maior valor de faturamento foi de {maior_valor}, ocorreu no dia {dia_maior_valor}.")


def valorMedio(dados):
    total = 0 # total dos valores sem os dias zerados
    dias_nao_zerados = 0 # dias que tem valor não zerados
    dias_maiores_media = 0 # dias que o valor foi maior que a media
    for i in dados:
        if i['valor'] != 0:
            total += i['valor']
            dias_nao_zerados += 1
    
    media = total/dias_nao_zerados
    for i in dados:
        if i['valor'] > media:
            dias_maiores_media += 1
    print(f'A media dos dias não zerados: {media}')
    print(f'O número de dias com valores maiores que a média é: {dias_maiores_media}')
    


menorValor(dados)
maiorValor(dados)
valorMedio(dados)