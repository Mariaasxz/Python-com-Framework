# Use dicionário, variáveis ou listas … 

# Contexto:
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:

# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")

# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico. 


# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# Reclamação 

# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)


dados = {
  'vip': input('VIP (sim ou nao): '),
 'valor': float(input('Valor da compra: ')),
    'primeira_compra': input('Primeira compra (sim ou nao): '),   'reclamacao': input('Tem reclamação? (sim ou nao): ')
}

resultado = (
      (
   dados['vip'] == 'sim' or
   dados['valor'] > 200 or
   dados['primeira_compra'] == 'sim'
    ) and dados['reclamacao'] == 'nao'
) and 'Cupom liberado' or 'Sem cupom'

print(resultado)