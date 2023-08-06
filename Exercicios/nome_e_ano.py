# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 
# 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que 
# completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará 
# o erro e continuará perguntando até que um valor correto seja preenchido.

nomeCompleto = input("Digite seu nome?")

identificacao = True

while(identificacao == True):
    print("Digeti seu ano de nascimento")
    try:
        anoNacimento = int(input())
        if (anoNacimento < 1922) or (anoNacimento > 2021):
            print("Digite um ano de nascimento entre 1922 e 2021")
        else:
            idade = 2021 - anoNacimento
            print("Seu nome é:", nomeCompleto, "sua idade é:", idade, "anos")

            identificacao = False
    except:
        print("Digite o ano do seu nascimento em números e dentro do intervalo por favor")

    



    

 