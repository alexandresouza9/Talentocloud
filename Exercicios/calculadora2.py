#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar 
#rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte 
#lista de operações:
#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair
#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
#o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

def calculadora(num1, num2, operacao):
    if (operacao == 1):
        return num1 + num2
    elif (operacao == 2):
        return num1 - num2
    elif (operacao == 3):
        return num1 * num2
    elif (operacao == 4):
        return num1 / num2
    else:
        return 0
resultado = calculadora (4, 7, 1)
print(resultado)

executar = True

while (executar == True):
   print("Qual a operação quer fazer")
   print("1: Soma 2: Subtração 3: Multiplicação 4: Divisão 0: Sair ")

   operacao = int(input())
   if (operacao < 0 ) or (operacao > 4):
      print("opção invalida")
   elif (operacao == 0):
      executar = False
   else:
      print("Digite o primeiro numero")
      num1 = int(input())
      print("Digite o segundo numero")
      num2 = int(input())

      resultado = calculadora (num1, num2, operacao)
      print("Resultado foi", resultado)

      