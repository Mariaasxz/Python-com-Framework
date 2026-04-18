# # # sistema de notas
# # print('SISTEMA DE NOTAS')
# # lista_nomes = []
# # aluno_1 =  input('Digite o nome do aluno: ')
# # aluno_2 =  input('Digite o nome do aluno: ')
# # lista_nomes.append(aluno_1)
# # lista_nomes.append(aluno_2)
# # print('lista de alunos: ', lista_nomes)

# # notas_aluno_1 = [float(input(f'nota1 {aluno_1}: ')), float(input(f'nota2 {aluno_1}: '))]
# # notas_aluno_2 = [float(input(f'nota1 {aluno_2}: ')), float(input(f'nota2 {aluno_1}: '))]

# # media_aluno_1 = sum(notas_aluno_1)/len(notas_aluno_1)
# # media_aluno_2  = sum(notas_aluno_2)/len(notas_aluno_2)
# # print('Aluno', aluno_1, 'Média', media_aluno_1)
# # print('Aluno', aluno_2, 'Média', media_aluno_2)

# # if media_aluno_1 > 6:
# #     print('Aluno aprovado', aluno_1)
# # elif media_aluno_1 >= 5 and media_aluno_1 <= 6:
# #     print('......................................')
# #     print('Aluno de recuperação', aluno_1)
# # else:
# #     print('Aluno reprovado', aluno_1)

# # print('.......................................')

# # if media_aluno_2 > 6:
# #     print('Aluno aprovado', aluno_2)
# # elif media_aluno_2 >= 5 and media_aluno_2 <= 6:
# #     print('Aluno de recuperação', aluno_2)
# # else:
# #     print('Aluno reprovado', aluno_2)






# ## **2 - Exercícios**

# ### **1. Classificação de Notas com Menção**

# Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:

# - `"Excelente"` se nota >= 9
# - `"Bom"` se nota >= 7 e < 9
# - `"Regular"` se nota >= 5 e < 7
# - `"Insuficiente"` se nota < 5

#Classificação de Notas 
# print('CLASSIFICAÇÃO DE NOTAS')
# # Leitura da nota
# nota = float(input("Digite a nota do aluno (0 a 10): "))

# # Classificação com base na nota
# if nota >= 9:
#     print("Excelente")
# elif nota >= 7:
#     print("Bom")
# elif nota >= 5:
#     print("Regular")
# else:
#     print("Insuficiente")



#  **2. Validação de Triângulo**

# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

# - `"Equilátero"` (todos os lados iguais)
# - `"Isósceles"` (dois lados iguais)
# - `"Escaleno"` (todos diferentes)

# print('Validação de Triângulo')
# lado_a= float(input("Lado A:"))
# lado_b= float(input("Lado B:"))
# lado_c= float(input("Lado C:"))

# if  lado_a== lado_b== lado_c:
#     print("equilatero")
# elif lado_a == lado_b or lado_a == lado_c or lado_c == lado_b:
#     print('isosceles')
# else:
#     print('escaleno')

### **3. Cálculo de IMC com Faixas**

# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

# - `"Abaixo do peso"` se IMC < 18.5
# - `"Peso normal"` se 18.5 ≤ IMC < 25
# - `"Sobrepeso"` se 25 ≤ IMC < 30
# # - `"Obesidade"` se IMC ≥ 30

    
# peso= float(input('peso (kg):'))
# altura= float(input('altura:'))

# imc = peso/(altura**2)

# if imc < 18.5:
#     print('abaixo do peso')
# elif imc < 25:
#      print('peso normal')
#  elif imc < 30:
#      print('sobre peso')
#  elif imc > 30:
#      print('obesidade')

#** 4 Calcular o salario liquido 

# def calcular_salario_liquido(salario_bruto):
#     # Desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00)
#     inss = min(salario_bruto * 0.11, 1500)
#     salario_com_inss = salario_bruto - inss
    
#     # Desconto do IRRF
#     if salario_com_inss <= 2500:
#         irrf = 0
#     elif salario_com_inss <= 3500:
#         irrf = (salario_com_inss - 2500) * 0.075
#     elif salario_com_inss <= 5000:
#         irrf = (salario_com_inss - 3500) * 0.15 + (1000 * 0.075)
#     else:
#         irrf = (salario_com_inss - 5000) * 0.275 + (1500 * 0.15) + (1000 * 0.075)
    
#     salario_liquido = salario_com_inss - irrf
#     return salario_liquido

# salario_bruto = float(input("Informe o salário bruto: R$ "))
# salario_liquido = calcular_salario_liquido(salario_bruto)
# print(f"Salário líquido após descontos: R$ {salario_liquido:.2f}")


#** 5 jogo Pedra, papel, tesoura 

def jogo_pedra_papel_tesoura(jogada1, jogada2):
    if jogada1 == jogada2:
        print("Empate")
    elif (jogada1 == "pedra" and jogada2 == "tesoura") or \
         (jogada1 == "tesoura" and jogada2 == "papel") or \
         (jogada1 == "papel" and jogada2 == "pedra"):
        print("Jogador 1 vence")
    else:
        print("Jogador 2 vence")

jogada1 = input("Jogada do jogador 1 (pedra, papel, tesoura): ").lower()
jogada2 = input("Jogada do jogador 2 (pedra, papel, tesoura): ").lower()

jogo_pedra_papel_tesoura(jogada1, jogada2)

#**6 Verificar aprovação 


def verificar_aprovacao(n1, n2, nr=None):
    media = (n1 + n2) / 2
    if media >= 7:
        print("Aprovado")
    elif media < 4:
        print("Reprovado")
    else:
        if nr is not None:
            media_final = (media + nr) / 2
            if media_final >= 5:
                print("Aprovado após recuperação")
            else:
                print("Reprovado após recuperação")
        else:
            print("Em recuperação")

n1 = float(input("Nota N1: "))
n2 = float(input("Nota N2: "))

verificar_aprovacao(n1, n2)
if (n1 + n2) / 2 >= 4 and (n1 + n2) / 2 < 7:
    nr = float(input("Nota da recuperação (NR): "))
    verificar_aprovacao(n1, n2, nr)

#**7 Verificar laistamento

def verificar_alistamento(ano_nascimento, sexo, deficiencia):
    if deficiencia == "sim":  # Corrigido: deve comparar a variável 'deficiencia' e não a string 'deficiencia'
        print("Dispensado por condição de saúde")
    else:
        idade = 2026 - ano_nascimento  # Corrigido: deve usar a variável 'ano_nascimento' e não a string 'ano_nascimento'
        if sexo == "F":  # Corrigido: deve comparar a variável 'sexo' e não a string 'sexo'
            print("Não obrigatório")
        elif sexo == "M":  # Corrigido: deve comparar a variável 'sexo' e não a string 'sexo'
            if idade < 18:
                print(f"Faltam {18 - idade} anos para o alistamento")
            elif idade == 18:
                print("Aliste-se imediatamente")
            elif idade <= 45:
                print("Já passou do prazo")
            else:
                print("Dispensado por idade")

# Leitura dos dados
ano_nascimento = int(input("Ano de nascimento: "))
sexo = input("Sexo (M/F): ").upper()
deficiencia = input("Possui alguma deficiência impeditiva? (sim/não): ").lower()

# Chamada da função
verificar_alistamento(ano_nascimento, sexo, deficiencia)

   
def calcular_plano_saude(idade, tipo_plano):
    if tipo_plano == "basico":
        valor = 100 + (idade * 2)
    elif tipo_plano == "standard":
        valor = 150 + (idade * 3)
    elif tipo_plano == "premium":
        valor = 200 + (idade * 5)
    else:
        print("Plano inválido")
        return

    if idade > 60:
        valor *= 1.10  # Acrescenta 10% para clientes acima de 60 anos
    
    print(f"Valor mensal do plano: R$ {valor:.2f}")

idade = int(input("Informe a idade: "))
tipo_plano = input("Tipo de plano (basico, standard, premium): ").lower()

calcular_plano_saude(idade, tipo_plano)

def is_bissexto(ano):
    return (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

def validar_data(dia, mes, ano):
    dias_por_mes = {
        1: 31, 2: 29 if is_bissexto(ano) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if mes < 1 or mes > 12:
        print("Mês inválido")
    elif dia < 1 or dia > dias_por_mes.get(mes, 0):
        print("Dia inválido")
    else:
        print("Data válida")

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

validar_data(dia, mes, ano)


