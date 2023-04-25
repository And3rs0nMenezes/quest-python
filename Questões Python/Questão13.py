#Q013-
lista = []

loop = True

while (loop):
    valor = input("Digite um valor numérico. Para parar, digite 'PARAR': ")

    if (valor == "PARAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print()

lista.sort()

for n in lista:
    print(f'Numeros na ordem crescente: {n}')
