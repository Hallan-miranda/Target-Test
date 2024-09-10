import json

json_data = '''
[
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
'''

faturamento_diario = json.loads(json_data)

def maior_valor(valores):
    maior_valor = 0
    for dia in valores:
        if dia['valor'] > maior_valor:
            maior_valor = dia['valor']
    print(f'Maior valor faturado em um dia foi de: R${maior_valor:.2f}')

def menor_valor(valores):
    menor_valor = 100000
    for dia in valores:
        if dia['valor'] < menor_valor and dia['valor'] != 0:
            menor_valor = dia['valor']
    print(f'Menor valor faturado em um dia foi de: R${menor_valor:.2f}')

def superio_media(valores):
    total_faturado= 0
    superior_media = 0
    dias_faturados = 0
    for dia in valores:
        if dia['valor'] > 0:
            total_faturado += dia['valor']
            dias_faturados += 1
    
    media_diaria = total_faturado / dias_faturados

    for dia in valores:
        if dia['valor'] > media_diaria:
            superior_media += 1

    print(f'Total de dias de faturamento superior a média diária: {superior_media} dias')
    print(f'Media diaria faturada: R${media_diaria:.2f}')


menor_valor(faturamento_diario)
maior_valor(faturamento_diario)
superio_media(faturamento_diario)