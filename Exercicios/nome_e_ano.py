# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 
# 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que 
# completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará 
# o erro e continuará perguntando até que um valor correto seja preenchido.


nomeCompleto = input("Qual seu nome?")
print(nomeCompleto)

anoNascimento = int(input("Digite o seu ano de nascimento"))
idade = 2021 - anoNascimento


while(anoNascimento == False):
    print("Digite um ano dentro o intervalo")
    try:
        anoNascimento = int(input())
        if (anoNascimento > 1922) and (anoNascimento < 2021):
            anoNascimento = True
            print("Seu nome é:", nomeCompleto, "sua idade é:", anoNascimento, "anos")
            #print("Você digitou um ano correto!")
        else:
            print("Você digitou um ano fora do intervalo")
    except:
        print("Caracter inválido, por favor digite um ano do seu nascimento")
    

 