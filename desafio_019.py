#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno_1 = input("Primeiro aluno: ")
aluno_2 = input("Segundo aluno: ")
aluno_3 = input("Terceiro aluno: ")
alunos=[aluno_1,aluno_2,aluno_3]
print("O aluno escolhido foi",random.choice(alunos))