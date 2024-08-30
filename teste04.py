dado = [
    {"estado": "SP","faturamento": 67836.43},
    {"estado": "RJ","faturamento": 36678.66},
    {"estado": "MG","faturamento": 29229.88},
    {"estado": "ES","faturamento": 27165.48},
    {"estado": "Outros","faturamento": 19849.53}
]
index = 0
total = 0
while index < len(dado):
    total += dado[index]['faturamento']
    index = index + 1


def calc_porcetagem(valor, total):
    index = 0
    quantidade_estado = len(valor)
    while index < quantidade_estado:
        porcentagem = round((valor[index]['faturamento'] / total) *100, 2)
        print(f'A porcentagem do faturamento mesal do estado {valor[index]['estado']} foi de {porcentagem}%')
        index += 1

calc_porcetagem(dado, total)