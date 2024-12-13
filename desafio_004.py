#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
usuario_texto = input("Digite alguma coisa:")
print("O tipo primitivo desse valor é",type(usuario_texto))
print("Só tem espaços?",usuario_texto.isspace())
print("É número?",usuario_texto.isnumeric())
print("É alfabético?",usuario_texto.isalpha())
print("É alfanumérico?",usuario_texto.isalnum())
print("Está em maiúsculas?",usuario_texto.isupper())
print("Está em minúsculas?",usuario_texto.islower())