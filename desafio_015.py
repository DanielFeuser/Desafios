#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input("Quantos dias alugados? "))
km = int(input("Quantos Km rodados? "))
dias_rodados = dias * 60
km_rodados = 0.15 * km
print(f"O total a pagar é de R${dias_rodados + km_rodados}")