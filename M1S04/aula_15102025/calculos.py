def calcular_total(consumos: list):
    """
        Função que calcula o total de consumo de água semanal.

        Entradas:
            consumos (list): lista de consumos diários de água.

        Saída:
            total (float): soma de todos os consumos.
    """

    return sum(consumos)

def calcular_media(consumos: list):
    """
        Função que calcula a média diária do consumo de água semanal.

        Entradas:
            consumos: list: lista ed consumos diários de água.

        Saída:
            total (float): a média diárias do consumo.

    """

    return sum(consumos) / len(consumos)

def avaliar_consumo(media: float):
    """
        Função para avaliar o consumo consúmo

        Entradas:
            media (float): média diária.

        Saída:
            String: avaliação do consumo.
    """

    if media < 150:
        return "Consumo a baixo da média sustentável."
    elif media <= 250:
        return "Consumo dentro da média sustentável."
    else:
        return "Consumo acima da média sustentável."