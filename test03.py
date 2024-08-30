faturamento_diario = [
    2950, 0, 4600, 2700, 3500, 3300, 4100, 3800, 4200, 0,
    3400, 2800, 4300, 0, 3700, 3000, 4600, 3900, 3100, 3200,
    4000, 0, 4200, 3500, 2900, 3100, 3700, 0, 4400, 3400
]

def maior_valor(valores):
    maior_valor = 0
    repeat = len(valores)
    index = 0
    while repeat > index:
        if faturamento_diario[index] > maior_valor:
            maior_valor = faturamento_diario[index]
        index += 1
    print(f'Maior valor faturado em um dia foi de: R${maior_valor:.2f}')

def menor_valor(valores):
    menor_valor = 100000
    repeat = len(valores)
    index = 0
    while repeat > index:
        if faturamento_diario[index] < menor_valor and faturamento_diario[index] > 0:
            menor_valor = faturamento_diario[index]
        index += 1
    print(f'Menor valor faturado em um dia foi de: R${menor_valor:.2f}')

def superio_media(valores):
    total_faturado= 0
    superior_media = 0
    dias_faturados = 0
    repeat = len(valores)
    index = 0
    
    while repeat > index:
        if valores[index] > 0:
            total_faturado += valores[index]
            dias_faturados += 1
        index += 1
    media_diaria = total_faturado / dias_faturados
    index = 0
    while repeat > index:
        if valores[index] > media_diaria:
            superior_media += 1
        index += 1
    print(f'Total de dias de faturamento superior a média diária: {superior_media} dias')
    print(f'Media diaria faturada: R${media_diaria:.2f}')


menor_valor(faturamento_diario)
maior_valor(faturamento_diario)
superio_media(faturamento_diario)