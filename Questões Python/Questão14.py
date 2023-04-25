#Q014-
lista = []

loop = True

while (loop):
    valor = input("Digite um valor. Para parar, digite 'PARAR': ")

    if (valor == "PARAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print()

lista = sorted(lista, key=int, reverse=True)

for n in lista:
    print(f'Numeros na ordem decrescente: {n}')
