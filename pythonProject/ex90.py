aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 5:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')