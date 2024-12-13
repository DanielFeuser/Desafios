#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura_parede = float(input("Digite a largura da sua parade em metros: "))
altura_parede = float(input("Digite a algura na sua parade em metros: "))
area_parede = altura_parede * largura_parede
quantidade_tinta = area_parede / 2
print(f"Sua parede tem a dimensão de{largura_parede}X{altura_parede} e a sua área é de {area_parede}m²")
print(f"A quantidade de tinta necessária para pintar sua parade é de {quantidade_tinta}litros")