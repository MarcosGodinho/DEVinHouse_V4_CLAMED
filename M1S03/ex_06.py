alunos_notas = {
    'João': [8.5, 9.0, 7.5],
    'Maria': [6.0, 5.5, 7.0],
    'Pedro': [10.0, 8.0, 9.5],
    'Ana': [5.0, 6.5, 4.0],
    'Lucas': [7.0, 7.0, 7.0],
    'Carla': [9.0, 8.8, 9.2],
    'Bruno': [4.5, 7.0, 5.0],
    'Juliana': [7.5, 8.0, 8.5],
    'Fernando': [6.5, 7.0, 8.0],
    'Beatriz': [3.0, 5.0, 4.5]
}

for aluno, nota in alunos_notas.items():
    mean = sum(alunos_notas[aluno]) / len(alunos_notas[aluno])
    if mean >= 7:
        print("Aluno: ", aluno," | Nota: ", nota, " | Média: ", format(mean, ".2f"), " - APROVADO")