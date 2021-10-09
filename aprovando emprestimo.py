# escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestaçao mensal,sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado

casa = float(input(' qual o valor da casa: R$  '))
salario = float(input(' qual seu salario: R$  '))
anos = int(input(' em quantos anos voçe quer pagar ? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R$ {:.2f} em {} anos '.format(casa , anos))
print(' a prestaçao sera de R$ {:.2f} '.format(prestaçao))
if prestaçao <= minimo:
    print(' emprestimo concedido')
else:
    print (' emprestimo negado')


