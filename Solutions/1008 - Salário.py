# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

ID = int(input())
hr_work = int(input())
hr_pay = float(input())

salary = hr_work * hr_pay

print("NUMBER =", ID)
print("SALARY = U$ {:.2f}".format(salary))
