import csv

with open("vendas.csv", "r") as arquivo_leitura, open("vendas_total.csv", "w", newline="") as arquivo_escrita:

    leitor = csv.reader(arquivo_leitura)
    escritor = csv.writer(arquivo_escrita)

    cabecalho = next(leitor)
    escritor.writerow(cabecalho + ["Total"])

    for produto, quantidade, valor in leitor:

        total = float(quantidade) * float(valor)
        escritor.writerow([produto, quantidade, valor, round(total, 2)])