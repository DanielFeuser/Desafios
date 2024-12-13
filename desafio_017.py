#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
a = float(input("Comprimento do cateto oposto: "))
b = float(input("Comprimento do cateto adjacente: "))
hipotenusa = round(math.sqrt(a**2 + b**2),2)
print(f"A hipotenusa vai medir {hipotenusa}")