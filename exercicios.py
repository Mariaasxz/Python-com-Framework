
# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.dispo = True

#     def emprestrar(self):
#       nome  = input('nome: ')
#     #   print(self.dispo)
#       emprestar =  input('Emprestar? ')
#       if emprestar == 'sim':
#         if nome  == self.titulo:
#             if self.dispo == True:
#                 print(self.dispo)
#                 print('esta disponivel ...')
#                 self.dispo = False
#                 print('Emprestado')
#                 return self.dispo

#             else:
#                 print('Não esta diponivel')
#         else:
#             print('Não temos esse livro...')
#     def devolver(self):
        
#         print('Livro devolvido')
#         return self.dispo
#     def info(self):
#         return [
#         self.titulo,
#         self.autor,
#         self.ano,
#         self.dispo 
#         ]


# livro =  Livro('Cisne negro', 'taleb','2012')
# livro.emprestrar()
# livro.devolver()
# print(livro.info())



#  Funcionario:
#     def __init__(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario_base = salario_base

#     def aumentar_salario(self, percentual):
#         self.salario_base = self.salario_base + (self.salario_base * percentual / 100)

#     def calcular_bonus(self):
#         return self.salario_base * 0.10

#     def exibir_dados(self):
#         print("Nome:", self.nome)
#         print("Cargo:", self.cargo)
#         print("Salário:", self.salario_base)
#         print("Bônus:", self.calcular_bonus())


# funcionario = Funcionario("Carla", "Atendente", 2000)

# funcionario.aumentar_salario(20)

# funcionario.exibir_dados()class





class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        if self.velocidade + valor <= 200:
            self.velocidade = self.velocidade + valor
        else:
            self.velocidade = 200

    def frear(self, valor):
        if self.velocidade - valor >= 0:
            self.velocidade = self.velocidade - valor
        else:
            self.velocidade = 0

    def velocidade_atual(self):
        print("Velocidade atual:", self.velocidade, "km/h")


carro = Carro("Toyota", "Corolla")

carro.acelerar(50)
carro.velocidade_atual()

carro.acelerar(100)
carro.velocidade_atual()

carro.acelerar(80)
carro.velocidade_atual()

carro.frear(70)
carro.velocidade_atual()

carro.frear(80)
carro.velocidade_atual()

carro.frear(100)
carro.velocidade_atual()