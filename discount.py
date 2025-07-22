preco = float(input('DIGITE O PREÇO DO PRODUTO A SER CALCULADO'))
p = int(input('DIGITE A PORCENTAGEM DE DESCONTO A SER APLICADA (0-100%)'))
desconto = preco * (p / 100)
final = preco - desconto
print('O Preço BASE é {}\n E o Desconto é de {}%'.format(preco, p))
print('O VALOR DO DESCONTO FOI DE: {}R$\n O VALOR FINAL É: {}R$'.format(desconto, final))