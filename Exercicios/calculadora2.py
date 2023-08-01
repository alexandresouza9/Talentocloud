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