import relatorio

print("==== Monitoramento de Consumo de Água ====")
print("Informe o consumo de água (em litros) para cada dia da semana:")

dias_semana = []

for i in range(7):
    dias_semana.append(float(input(f"Dia {i+1}: ")))

relatorio.gerar_relatorio(dias_semana)
