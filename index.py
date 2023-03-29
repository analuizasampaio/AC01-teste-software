# Nome: Ana Luiza Sampaio RA: 2101183
# Nome: Guilherme Portes Bebiano  RA: 2101494
# Nome: Ingrid Priscila Alves de Sousa RA: 2101204
# Nome: Charles Eduardo Felipe de Souza RA:  2100038
# Nome: Kauê Ribeiro Varjão RA: 1904284

dicionario = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def converte(simbolo):
    summ = 0
    for i in range(len(simbolo)-1, -1, -1):
        num = dicionario[simbolo[i]]
        if 3*num < summ:
            summ = summ-num
        else:
            summ = summ+num
    return summ
