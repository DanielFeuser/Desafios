#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Digite o ângulo que você deseja: "))
print(angulo)
angulo_radianos = math.radians(angulo)
seno = round(math.sin(angulo_radianos),2)
cosseno = round(math.cos(angulo_radianos),2)
tangente = round(math.tan(angulo_radianos),2)
print(seno, cosseno, tangente)
