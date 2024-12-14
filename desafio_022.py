#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
'''
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
'''

nome=str(input("Qual seu nome completo: ")).strip()
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
letras_nome= len(nome) - nome.count(" ")
print("Analizando seu nome...")
print("Seu nome em maiúsculo é",nome_maiusculo)
print("Seu nome em minusculo é",nome_minusculo)
print(f"Seu nome tem ao todo {letras_nome} letras")
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0],len(separa[0])))