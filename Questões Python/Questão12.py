#Q012-
lista = []

loop = True

while (loop):
    valor = input("Digite um valor. Para parar, digite 'PARAR': ")

    if (valor == "PARAR"):
        loop = False
    else:
        valorNumerico = int(valor)
        lista.append(valorNumerico)

print(f'Soma dos números: {sum(lista)}')