#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
n = float(input("Digite um valor: "))
print("O valor digitado foi {} e sua porção inteira é {}".format(n,int(n)))