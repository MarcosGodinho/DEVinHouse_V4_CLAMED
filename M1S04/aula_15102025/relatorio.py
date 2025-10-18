import calculos as calc

def gerar_relatorio(dias_semana: list):
    """
    Função para gerar o relatório com Total semanal, média diária e a avaliação.

    Entradas:
        dias_semana (list): lista de consumos diários de água.

    Saída:
        String com relatório de consumo de água.

    """

    print("\n==== Relatório de Consumo de Água ====")
    print(f"Total semanal: {calc.calcular_total(dias_semana)} L")
    print(f"Média diária: {calc.calcular_media(dias_semana):.2f} L")
    print(f"Avaliação: {calc.avaliar_consumo(calc.calcular_media(dias_semana))}")
    print("=======================================")
