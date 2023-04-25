#Q010-
lista = []

loop = True

while (loop):
    valor = input("Digite um valor. Para parar, digite 'PARAR': ")

    if (valor == "PARAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

for n in lista:
    if n % 2 == 0:
        print(f'PAR: {n}')
