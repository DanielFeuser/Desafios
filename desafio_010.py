#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
carteira = float(input("Digite o valor que você tem na carteira? R$ "))
dolar = 6.00
quantidade = round((carteira/dolar),2)
print(f"Com esse valor você consegue comprar US$ {quantidade}")