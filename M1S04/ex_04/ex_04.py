# lista de números pra testar
numeros = [15, 8, 22, 10, 30, 5, 18]

# função que calcula a média
def calcular_media(lista_de_numeros):
    # round() serve pra limitar em 2 casas decimais
    media = round(sum(lista_de_numeros) / len(lista_de_numeros), 2)
    return media

# função que acha o maior e o menor valor
def encontrar_maior_menor(lista_de_numeros):
    maior = max(lista_de_numeros)
    menor = min(lista_de_numeros)
    # retorna os dois valores de uma vez
    return maior, menor

# função principal que organiza as chamadas e mostra os resultados
def funcao_principal():
    # chama a função da média e guarda o resultado
    media_calculada = calcular_media(numeros)
    print(f"A média dos valores é: {media_calculada}")

    # aqui a gente pega os dois valores que a função de cima retornou
    maior_valor, menor_valor = encontrar_maior_menor(numeros)
    print(f"O maior valor é: {maior_valor}")
    print(f"O menor valor é: {menor_valor}")

# chama a função principal pra rodar tudo
funcao_principal()