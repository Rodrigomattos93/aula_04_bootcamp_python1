dicionario_recebido: dict = {
    'nome': 'Rodrigo',
    'nascimento': 1993,
    'gênero': 'M',
    'naturalidade': 'ES'
}

def retorna_lista_key_ordenadas(entrada_dict: dict) -> list:
    saida = sorted(list(entrada_dict.keys()))
    return print(saida)

retorna_lista_key_ordenadas(dicionario_recebido)
