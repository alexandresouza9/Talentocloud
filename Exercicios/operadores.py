numero1 = input("Digite o número 1 ")
numero1 = int(numero1)

numero2 = input("Digite o número 2 ")
numero2 = int(numero2)

if(numero1 == numero2): #operador de igualdade
    print("O número %d é igual a %d. "% (numero1, numero2))
if(numero1 != numero2): #operador de diferente
    print("O número %d é diferente de %d "% (numero1, numero2))
if(numero1 < numero2): #operador de menor que
    print("O número %d é menor que o %d "% (numero1, numero2))
if(numero1 > numero2): #operador de maior que
    print("O número %d é maior que o %d "% (numero1, numero2))
if(numero1 <= numero2): #operador de menor ou igual
    print("O número %d é menor ou igual %d "% (numero1, numero2))
if(numero1 >= numero2): #operador de maior ou igual
    print("O número %d é maior ou igual %d "% (numero1, numero2))    

