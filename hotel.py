#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

andar=0
#primeiro código
if andar==0:
  print('Térreo')
for andar in range(1, 13):
  print(andar,'º Andar')
# segundo código
print("ordem decrescente")
for andar in range(20, 0, -1):
  print(andar,'º Andar')
