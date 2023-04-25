#Q08-
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

lista.sort()


print(f'Menor valor: {lista[0]}')
print(f'Maior valor: {lista[len(lista) - 1]}')