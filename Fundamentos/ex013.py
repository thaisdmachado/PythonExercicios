salario = float(input('Qual o salário do Funcionário? R$'))
reajustado = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, reajustado))