#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int(input("Digite um número: "))
print(f"O dobro desse número é {n*2}\nO triplo desse número é {n*3}\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")