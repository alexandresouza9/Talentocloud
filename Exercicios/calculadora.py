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