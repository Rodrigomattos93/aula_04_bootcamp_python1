numero = int(input("Insira um número para verificar se é primo: "))

def verificar_se_o_numero_eh_primo(entrada: int) -> bool:
    qtd_divisores: int = 0
    for divisor in range(1, entrada):
        if entrada % divisor == 0:
            qtd_divisores = qtd_divisores + 1
    
    if qtd_divisores == 1:
        saida = True
    else:
        saida = False

    return print(saida)

verificar_se_o_numero_eh_primo(numero)