from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data = input("Digite a data (dd/mm/yyyy): ")
data_formatada = datetime.strptime(data, "%d/%m/%Y")
print(data_formatada.strftime("%d/%m/%Y"))

ultimo_dia = datetime(data_formatada.year, 12, 31)
print(ultimo_dia.strftime("%d/%m/%Y"))

print("Dias até o último dia do ano :", (ultimo_dia - data_formatada).days)
print("Dia da semana :", data_formatada.strftime("%A"))