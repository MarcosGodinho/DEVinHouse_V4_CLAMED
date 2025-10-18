import csv
import re

lista_emails = [
    "usuario@example.com",
    "usuario.nome@example.co.uk",
    "primeiro.ultimo@sub.dominio.org",
    "usuario+tag@gmail.com",
    "aluno-123@faculdade.edu.br",
    "contato@site-legal.net",
    "a@b.co",

    "invalido-sem-arroba.com",
    "outro@dominio-invalido",
    "sem-dominio@",
    "usuario@.com",
    "maria@hotmail.",
    "email.@example.com",
    "email..invalido@example.com",
    "usuário_com_acento@example.com",
    "muito longo................................................................@example.com",
    "email@123.123.123.123"
]

with open("emails_validos.txt", "w", newline="") as validos, open("emails_invalidos.txt", "w", newline="") as invalidos:

    escritor_validos = csv.writer(validos)
    escritor_invalidos = csv.writer(invalidos)

    for email in lista_emails:
        padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(padrao, email):
            escritor_validos.writerow([email])
        else:
            escritor_invalidos.writerow([email])