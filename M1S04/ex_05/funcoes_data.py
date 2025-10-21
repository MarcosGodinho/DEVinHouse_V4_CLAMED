import locale
from datetime import datetime

def dias_ate_ano_novo(data):

    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    ultimo_dia = datetime(data_formatada.year, 12, 31)
    return (ultimo_dia - data_formatada).days

def dias_desde_comeco_ano(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    primeiro_dia = datetime(data_formatada.year, 1, 1)
    return (data_formatada - primeiro_dia).days

def dia_semana(data):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    return data_formatada.strftime("%A")

def dias_ate_natal(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    natal = datetime(data_formatada.year, 12, 25)
    return (natal - data_formatada).days

def dias_ate_proximo_aniversario(data_aniversario):

    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    data_nascimento = datetime.strptime(data_aniversario, "%d/%m/%Y")
    aniversario_neste_ano = datetime(hoje.year, data_nascimento.month, data_nascimento.day)

    if aniversario_neste_ano < hoje:
        proximo_aniversario = datetime(hoje.year + 1, data_nascimento.month, data_nascimento.day)
    else:
        proximo_aniversario = aniversario_neste_ano

    return (proximo_aniversario - hoje).days