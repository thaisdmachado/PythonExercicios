dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
valordias = dias * 60
valorkm = km * 0.15
valorfinal = valordias + valorkm
print('O total a pagar é de R${:.2f}'.format(valorfinal))