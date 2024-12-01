a = input("Digite um número inteiro: ")
b = input("Digite outro número inteiro: ")

a1 = int(a)
b1 = int(b)

soma = str(a1 + b1)
sub = str(a1 - b1)
mult = str(a1 * b1)
power = str(a1 ** b1)
div = str(a1 / b1)
mod = str(a1%b1)

toString = ("\n Valor a: " + a + ";\n Valor b: " + b +";\n Soma: " + soma + ";\n Subtração: " + sub + ";\n Multiplicação: " + mult + ";\n Potenciação: " + power + ";\n Divisão: " + div + ";\n Módulo: " + mod + ".\n")

print(toString)