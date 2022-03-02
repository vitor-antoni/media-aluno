cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'limpar': '\033[m'}
turma = []
cont_aluno = 0
titulo = f'{cores["verde"]}Conselho de classe{cores["limpar"]}'
print('-=' * 20)
print(titulo.center(50))
print('-=' * 20)
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
    continuar = str(input(f'Deseja adicionar outra pessoa [{cores["verde"]}S{cores["limpar"]}/{cores["vermelho"]}N{cores["limpar"]}]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input(f'Dígito inválido! Deseja adicionar outra pessoa [{cores["verde"]}S{cores["limpar"]}/{cores["vermelho"]}N{cores["limpar"]}] ')).upper().strip()[0]
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
    if media < 6:
        print(f'A média do aluno está {cores["vermelho"]}inadequada!{cores["limpar"]}')
    elif media > 6 and media < 8:
        print(f'A média do aluno está {cores["amarelo"]}regular{cores["limpar"]}!')
    elif media >= 8 and media < 10:
        print(f'A média do aluno está {cores["azul"]}adequada{cores["limpar"]}!')
    else:
        print(f'A média do aluno está {cores["verde"]}excelente!{cores["limpar"]}')
    mais = str(input('Deseja saber a nota de mais alguém [S/N]? ')).upper().strip()[0]
    while mais not in 'SN':
        mais = str(input('Dígito inválido! Deseja saber a nota de mais alguém [S/N]? ')).upper().strip()[0]
    if mais == 'N':
        break
if mais == 'N':
    print(f'\nAs notas solicitadas foram {cores["verde"]}visualizadas{cores["limpar"]}!')
else:
    print(f'\nForam visualizadas as notas de {cores["verde"]}todos{cores["limpar"]} os alunos!')