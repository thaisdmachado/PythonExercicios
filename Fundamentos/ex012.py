preco = float(input('Qual o preço do produto? R$'))
novopreco = preco - (preco * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% irá custar R${:.2f}'.format(preco, novopreco))