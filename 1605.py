# # # import random 

# # # n = random.random()
# # # print(n)










# # #jogador 
# # # class jogador:
# # #  def escolher(self):
# # #     opção = ['pedra', 'papel', 'tesoura']
# # #     return random.choice(opção)


# # # # jogo 
# # # class jogo:
# # #     def verificar_vencedor(self, jogador, computador):
# # #         if jogador==computador:
# # #             return 'empate'
# # #             if jogador==





# # # jogo com programação
# # # pedra papel com POO
# # import random

# # # jogador
# # class Jogador:
# #     def escolher(self):
# #         escolha = input('Escolha pedra,papel ou tesoura')
# #         return escolha.lower()
# # # computador
# # class Computador:
# #     def escolher(self):
# #         opcao = ['pedra','papel','tesoura']
# #         return random.choice(opcao)
    
# # class Jogo:

# #     def verificar_vencedor(self, jogador, computador):
# #         score_jogador = 0
# #         score_computador = 0
# #         if jogador == computador:
# #             print(score_jogador, 'x', score_computador)
# #             return 'empate'
# #         if jogador == 'pedra' and computador == 'tesoura':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         elif jogador == 'tesoura' and computador  == 'papel':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         elif jogador == 'papel'  and computador == 'pedra':
# #             score_jogador =  score_jogador + 1
# #             print(score_jogador, 'x', score_computador)
# #             return 'Jogador venceu'
# #         else:
# #             score_computador =  score_computador + 1
# #             print(score_jogador, 'x', score_computador)
# #             print()
# #             return 'Computador venceu...'
# #     def jogar(self):
            
# #             while True:
# #                 jogador  = Jogador()
# #                 computador = Computador()
# #                 escolha_jogador  = jogador.escolher()
# #                 escolha_computador  = computador.escolher()
# #                 print('Jogador escolheu - ', escolha_jogador)
# #                 print('Computador escolheu - ', escolha_computador)
# #                 resultado = self.verificar_vencedor(escolha_jogador, escolha_computador)
# #                 print('RESULTADO', resultado)
        
# # jogo = Jogo()
# # jogo.jogar()



# # class

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.emprestado = False
        
#     def emprestar(self):
#         if not self.emprestado:
#             self.emprestado = True
#             return self.emprestado
            
            
#     def devolver(self):
#         self.emprestado = False         
#         return self.emprestado
    
#     def __str__(self):
#         return f'{self.titulo} {self.autor} {self.ano}'

# titulo, autor, ano = input('Livro: '), input('autor: '), input('ano ')

# l1 =  Livro(titulo, autor, ano)

# print('Emprestado? - ', l1.emprestar())

# print('Emprestado? - ',l1.devolver())

# print(l1)





# class Contador:
#     total_contadores = 0
#     def __init__(self):
#         Contador.total_contadores += 1
        
#     def exibir_total(self):
#         print(Contador.total_contadores)
        
# c1 =  Contador()
# c2 =  Contador()
# c3 =  Contador()
# c4 =  Contador()
        




class Aluno:
    def __init__(self, nome, matricula):
        self.nome  = nome
        self.matricula =  matricula 
        self.__notas = []

    def adcionar_notas(self, nota):
        if 0 <= nota <= 10 :
            self.__notas.append(nota)
            
    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def situacao(self):
        media  =  self.calcular_media()
        if media >= 7:
            return 'Aprovado'
        elif media >= 5:
            return 'Recuperação'
        else:
            return 'Reprovado'

aluno1 = Aluno('Ana', '1')
aluno2 = Aluno('Julia', '2')

aluno1.adcionar_notas(8)
aluno1.adcionar_notas(5)
aluno1.adcionar_notas(10)

aluno2.adcionar_notas(1)
aluno2.adcionar_notas(2.5)
aluno2.adcionar_notas(10)

print('Média',aluno1.nome ,aluno1.calcular_media())
print('Média',aluno2.nome ,aluno2.calcular_media())

print(aluno1.situacao())
print(aluno2.situacao())