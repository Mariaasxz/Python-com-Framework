# try:
#     n  =  int(input('>>'))
#     print(10/n)
# except ZeroDivisionError as erro:
#     print('error')


    # try:
#    tente fazer isso 
# except:
#    isso não funcionar mostre 
# else:
#    erro não identificado ou sem erros
# finally:
#    sempre carrega   

# qualidade do código 
# trazer organização
# otimizar o tratamento de erros

# var =  10
# x =  100

# indentação  = organização do código

# try:
 
    
#     print(10 + 10)
#     l = [1,2,3,5]
#     y  = l[5]
#     print(y)
    
# except NameError as erro:
#     print(erro)
# except ValueError as erro:
#     print(erro)

# except IndexError as erro:   
#     print(erro)     
    
# else:
#     print('ocorreu um não identificado ou não houve erro')
   
# finally:
#     print('fim  decarregamento...')
   



# lista =  [1,2,3]

# print(lista[0]/0)

try:
    n1  = int(input('>>>'))
    n2  =  int(input('>>'))
    soma  =  n1 + n2
    lista  =  [n1, n2]
    i =  int(input('Indice: '))
    print(lista[i])
    numero =  int(input('numero:  '))
    print(float(numero))
    print(n1/n2)
    
except TypeError as erro:
    # tentando fazer o calculo aritmético
    # entre um numero e uma letra...
    print(erro)
except ValueError as erro:
    # quando tento imprimir uma letra em um input de numero
    print(erro)
except IndexError as erro:
    # indice que não existe na lista
    print(erro)
except ZeroDivisionError as erro:
    print(erro)
else:
    print('Erro não identificado')
finally:
    print('fim carregamento...')
