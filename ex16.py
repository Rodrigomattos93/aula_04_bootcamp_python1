lista_numeros: list = input("insira uma lista de números: ").split(",")



def soma_todos_os_numeros(lista: list) -> int:
    soma: int = 0
    for i in range(0, len(lista)):
        lista[i] = int(lista_numeros[i])
        soma = lista[i] + soma
    
    return print(soma)

soma_todos_os_numeros(lista_numeros)


