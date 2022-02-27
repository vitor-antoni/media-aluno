turma = []
cont_aluno = 0
while True:
    aluno = str(input('Digite o nome do aluno: '))
    turma.append([f'{aluno}'])
    nota_1 = float(input('Digite sua primeira nota: '))
    while nota_1 > 10:
        nota_1 = float(input('Nota digitada inválida! Sua nota deve estar entre 0 e 10. Tente novamente: '))
    turma[cont_aluno].append(nota_1)    # Adiciona na lista, a nota do aluno de acordo com a contagem
    nota_2 = float(input('Digite sua segunda nota: '))
    while nota_2 > 10:
        nota_2 = float(input('Nota digitada inválida! Sua nota deve estar entre 0 e 10. Tente novamente: '))
    turma[cont_aluno].append(nota_2)
    cont_aluno += 1
    continuar = str(input('Deseja adicionar outra pessoa [S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dígito inválido! Deseja adicionar outra pessoa [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Número |  Nome')
for num, c in enumerate(turma):
    # print(c) retorna a lista inteira, uma por uma
    print(f'  {num}    |  {c[0]}')
for c in turma:
    escolha = int(input('Qual pessoa você deseja saber a média? '))
    media = (turma[escolha][1] + turma[escolha][2]) / 2     
    print(f'A média de {turma[escolha][0]} é {media}')     # Turma == lista / Escoha == sublista / 0 == nome
    mais = str(input('Deseja saber a nota de mais alguém [S/N]? ')).upper().strip()[0]
    while mais not in 'SN':
        mais = str(input('Dígito inválido! Deseja saber a nota de mais alguém [S/N]? ')).upper().strip()[0]
    if mais == 'N':
        break
if mais == 'N':
    print('\nAs notas solicitadas foram visualizadas!')
else:
    print('\nForam visualizadas as notas de todos os alunos!')