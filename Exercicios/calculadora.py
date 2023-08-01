#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá 
# a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

print("Digite um numero1")
numero1 = int(input())

print("Digite o operador")
operador = input()

if operador == "+":
    numero2 = 10
    numero3 = 30
    resultado = numero1 + numero2 + numero3
    print(resultado)
    
elif operador == "-":
    numero2 = 10
    numero3 = 30
    resultado = numero3 - numero2 - numero1
    print(resultado)
elif operador == "*":
    numero2 = 10
    numero3 = 20
    resultado = numero3 * numero2 * numero1
    print(resultado)
elif operador == "/":
    numero2 = 10
    numero3 = 50
    resultado = (numero3 + numero2) / numero1
    print(resultado)
else:
    print("Operador invalido")