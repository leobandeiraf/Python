#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

salarioHr = float(input())
trabalhoHr = float(input())

salario = salarioHr * trabalhoHr

print(f"O salário bruto mensal é de R${round(salario, 2)}")
