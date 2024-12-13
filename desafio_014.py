#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura_c = float(input("Informe a temperatuda em °C: "))
temperatura_f = (temperatura_c * 1.8) +32
print(f"A temperatura de {temperatura_c}°C corresponde a {temperatura_f}°F")