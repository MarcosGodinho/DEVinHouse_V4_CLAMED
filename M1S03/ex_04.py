nomes = ["Marcos", "Eduardo", "Lucas", "Gustavo", "Alberto", "Miguel", "Carlos"]
idades = [20, 14, 19, 18, 24, 25, 23]

dicionario = {}

for nome, idade in zip(nomes, idades):
    dicionario[nome] = idade

print(dicionario)
