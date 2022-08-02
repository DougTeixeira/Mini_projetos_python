def fatuMensal(estados):
    estados = dict(estados)
    faturamento_total = 0

    for valor in estados.values():
        faturamento_total += float(valor)

    print(f'O faturamento total: {faturamento_total}')
    
    porcentual_estados = {}
    for k, v in estados.items():
        porcentual_estados[k] = f'{(float(v)/faturamento_total)*100}%'
    print(f'O porcentual do faturamento por estado:')
    
    for k, v in porcentual_estados.items():
        print(f'{k}: {v}')


estados = {'SP ': '67.83643', 'RJ': '36.67866', 'MG': '29.22988', 'ES': '27.16548', 'Outros': '19.84953'}
fatuMensal(estados)