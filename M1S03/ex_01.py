dicionario = {
    "iPhone" : 1000.00,
    "iPad" : 1300.00,
    "Fones de Ouvido" : 250.00,
    "Cabo HDMI" : 10.00,
    "Teclado Mecânico" : 150.00,
    "Teclado Membrana" : 50.00,
    "Caixas de Som" : 25.00,
}

for prod in dicionario:
    if dicionario[prod] > 100:
        print(prod, "-", dicionario[prod])