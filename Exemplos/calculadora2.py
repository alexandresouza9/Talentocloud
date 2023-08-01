while opcao!= 0:
    opcao = int (input("[1]Soma \n[2]Subtracao \n[3]Mutiplicacao \n[4]Divisao\n[0] Sair \n: "))

    def calculadora(num1, num2, operacao):
    
      if opcao == 1:
        if (operacao == 1):
           return num1 + num2 
      elif opcao == 2:
        if (operacao == 2):
          return num1 - num2
      elif opcao == 3:
        if (operacao == 3):
          return num1 * num2
      elif opcao == 4:
        if (operacao == 4):
          return num1 / num2
      else:
        return 0
resultado = calculadora (4, 7, 1)
print(resultado)  