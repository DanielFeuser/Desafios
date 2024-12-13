#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_funcionario = float(input("Qual é o salário do Funcionário?: R$"))
aumento = round(((15/100)*salario_funcionario),2)
print(f"Um funcionário que ganhava R${salario_funcionario}, com 15% de aumento, passa a receber R${salario_funcionario+aumento}")