string_recebida = input("digite um texto para invertê-lo: ")

def inverter_texto(entrada: str) -> str:
    saida = entrada[::-1]
    return print(saida)

inverter_texto(string_recebida)