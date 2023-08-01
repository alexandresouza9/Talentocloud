rodas = 0
peso = 0
qtd_pessoas = 0

rodas = int(input("Quantas rodas tem veículo? "))
peso = float (input("Qual o peso bruto do veiculo? "))
qtd_pessoas = int(input("Qual é o maior número de pessoas que o veículo acomada? "))

if rodas <= 3:
    print("Melhor categoría de CNH: A")
elif rodas == 4 and qtd_pessoas <= 8 and peso <= 3500:
    print("Melhor categoría de CNH: B")
elif peso <= 3500 and peso <= 6000:
     print("Melhor categoría de CNH: C")
elif qtd_pessoas > 8:
     print("Melhor categoría de CNH: D")
else:
     print("Melhor categoría de CNH: E") 