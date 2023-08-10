def mostrarNumero():
    
    numeroValido = False
    print("Digite um número menor ou igual a 100")
    while(numeroValido == False):
        try:        
            num = int(input())
            if (num > 100):
                print("O número digitado tem que ser menor ou igual a 100!!")
            else:
                print("O número que você escolheu foi:" + str (num) )
                numeroValido == True
        except:
            print("O valor digitado deve ser inteiro")
mostrarNumero()