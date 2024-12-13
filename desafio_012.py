#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Qual o preço desse produto sem o desconto de 5%?: R$"))
desconto = round(((5 / 100)*preco),2)
print(f"O produto que custava R${preco}, na promoção com desconto de 5% vai custar R$ {preco - desconto}")