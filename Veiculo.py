opcao = - 1

while opcao!= 0:
    opcao = int (input("[1]Veículos com duas ou três rodas \n[2]Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg \n[3]Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg \n[4] Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg \n[0] Sair \n: "))
    
    if opcao == 1:
        print("CNH A")
    if opcao == 2:
        print("CNH B")
    if opcao == 3:
        print("CNH C")
    elif opcao == 4:
        print("CNH D")




