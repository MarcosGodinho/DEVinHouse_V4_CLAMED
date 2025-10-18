qtd_alunos = int(input("Digite a quantidade de alunos: "))
all_alunos = {}

for i in range(qtd_alunos):
    nome = input("Digite o nome do aluno: ")

    notas = []
    for j in range(1,4):

        while True:
            print(f"Digite a #{j} nota: ")
            nota = float(input())

            if nota >= 0 and nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Tente novamente.")

    all_alunos[nome] = notas

print("Alunos cadastrados com sucesso!!")

medias = {}

for aluno, notas in all_alunos.items():
    media = sum(notas) / len(notas)

    medias[aluno] = media

aprovados = []
reprovados = []

for aluno, media in medias.items():
    info_aluno = {'nome': aluno, 'media': media}

    if media >= 7:
        aprovados.append(info_aluno)
    else:
        reprovados.append(info_aluno)

print("\n--- RESULTADO FINAL ---")
print("Aprovados:")
for aluno in aprovados:
    print(f"  - {aluno['nome']}: média {aluno['media']:.2f}")

print("\nReprovados:")
for aluno in reprovados:
    print(f"  - {aluno['nome']}: média {aluno['media']:.2f}")