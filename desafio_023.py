#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero =int(input("Digite um número de 0 a 9999: "))
unidade = numero % 10
resto = numero //10
dezena = resto % 10
resto = numero//100
centena = resto%10
resto = numero//1000
milhar = resto
print(f"Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}")