#sistema de notas 
print("SISTEMA DE NOTAS")

lista_nomes = []
aluno_1 =input('digite o nome do aluno: ')
aluno_2 =input('digite o nome do aluno: ')
lista_nomes.append(aluno_1)
lista_nomes.append(aluno_2)
print('lista de alunos:' , lista_nomes)

notas_aluno_1 = [float(input('nota1:'))]
notas_aluno_2 = [float(input('nota2:'))]

media_aluno_1 = sum(notas_aluno_1)/len(notas_aluno_1)
media_aluno_2 = sum(notas_aluno_2)/len(notas_aluno_2)
print('Aluno' , aluno_1, 'Media', media_aluno_1)
print('Aluno' , aluno_2, 'Media', media_aluno_2)

if media_aluno_1 > 6: 
    print('aluno aprovado')
elif media_aluno_1 >= 5 and media_aluno_1 <= 6 :
    print('Aluno de recuperaçao')

    # sistema de notas
print('SISTEMA DE NOTAS')
lista_nomes = []
aluno_1 =  input('Digite o nome do aluno: ')
aluno_2 =  input('Digite o nome do aluno: ')
lista_nomes.append(aluno_1)
lista_nomes.append(aluno_2)
print('lista de alunos: ', lista_nomes)

notas_aluno_1 = [float(input(f'nota1 {aluno_1}: ')), float(input(f'nota2 {aluno_1}: '))]
notas_aluno_2 = [float(input(f'nota1 {aluno_2}: ')), float(input(f'nota2 {aluno_1}: '))]

media_aluno_1 = sum(notas_aluno_1)/len(notas_aluno_1)
media_aluno_2  = sum(notas_aluno_2)/len(notas_aluno_2)
print('Aluno', aluno_1, 'Média', media_aluno_1)
print('Aluno', aluno_2, 'Média', media_aluno_2)

if media_aluno_1 > 6:
    print('Aluno aprovado', aluno_1)
elif media_aluno_1 >= 5 and media_aluno_1 <= 6:
    print('Aluno de recuperação', aluno_1)
else:
    print('Aluno reprovado', aluno_1)

print('.......................................')

if media_aluno_2 > 6:
    print('Aluno aprovado', aluno_2)
elif media_aluno_2 >= 5 and media_aluno_2 <= 6:
    print('Aluno de recuperação', aluno_2)
else:
    print('Aluno reprovado', aluno_2)


    





