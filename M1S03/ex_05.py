compras_joao = ['maçã', 'banana', 'leite', 'pão', 'café', 'arroz', 'queijo']
compras_maria = ['leite', 'pão', 'ovos', 'chocolate', 'banana', 'suco', 'manteiga']

# Itens em comum:
print("Compras que João e Maria tem em comum: ", set(compras_joao).intersection(compras_maria))

# Itens exclusivos de cada um:
print("Itens exclusivos do João: ", set(compras_joao).difference(set(compras_maria)))
print("Itens exclusivos da Maria: ", set(compras_maria).difference(set(compras_joao)))

# Todos os itens sem duplicadas
print("Itens sem duplicadas: ", set(compras_joao).symmetric_difference(set(compras_maria)))


######################################
print("\nOutra forma de fazer\n")

cj = set(compras_joao)
cm = set(compras_maria)

# Itens em comum
print("Itens em comum: ", cj & cm)

# Itens exclusivos de cada um
print("Itens exclusivos do João: ", cj - cm)
print("Itens exclusivos da Maria: ", cm - cj)

# União
print("Todos os itens (união): ", cj | cm)

# Diferença Simétrica
print("Itens que não se repetem em nenhuma lista: ", cj ^ cm)
