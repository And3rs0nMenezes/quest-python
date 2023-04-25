#Q07-
def fibonnaci(numero):
    if numero < 2:
        return numero
    return fibonnaci(numero - 1) + fibonnaci(numero - 2)


resultado = fibonnaci(int(input("Escolha um número: ")))

print(f'Sequência de fibonnaci : {resultado}')