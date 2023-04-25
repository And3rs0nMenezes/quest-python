#Q09-
from statistics import mean

lista = []

loop = True

while (loop):
    valor = input("Digite um valor. Para parar, digite 'PARAR': ")

    if (valor == "PARAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print(f'Média: {mean(lista)}')