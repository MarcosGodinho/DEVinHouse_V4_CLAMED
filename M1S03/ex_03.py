# Criação da tupla
tupla_elementos = (1, 2, 3, 4, 5)

# Tentativa de alterar o elemento no index 1

# O erro que aparece é o:
# TypeError: 'tuple' object does not support item assignment
tupla_elementos[1] = 4



# TypeError: 'tuple' object doesn't support item deletion
del tupla_elementos[1]

# Isso significa que o tipo tupla não suporta a alteração (nem deleção) de seus elementos