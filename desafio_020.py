#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno_1 = input("Primeiro aluno: ")
aluno_2 = input("Segundo aluno: ")
aluno_3 = input("Terceiro aluno: ")
aluno_4 = input("Quarto aluno: ")
alunos=[aluno_1,aluno_2,aluno_3,aluno_4]
random.shuffle(alunos)
print("A ordem de apresentação será\n",alunos)