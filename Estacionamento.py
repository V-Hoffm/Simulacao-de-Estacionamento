import numpy as np
import random

A = np.array([1, 2, 3, 4, 5])
B = np.array([6, 7, 8, 9, 10])
C = np.array([11, 12, 13, 14, 15])
Vagas_ocupadas = np.empty(16,dtype=object)
Placas = np.empty(16,dtype=object)
vaga = [] 
cont = -1
cont_vga = 0
while True:
    print (f"Existem {cont_vga} vagas ocupadas neste estacionamento")
    qt = np.count_nonzero(Vagas_ocupadas == None)
    if qt == 1:
        print ("Todas as vagas estão ocupadas...")
        break     
    vaga = random.randint(1, 15)
    if vaga in A:
        setor = "A"
    elif vaga in B:
        setor = "B"
    else:
        setor = "C"
    print(f"A vaga sorteada foi a vaga {vaga}, no setor {setor}")

    if vaga in Vagas_ocupadas:
        print("Vaga já ocupada, sorteando outra...")
        continue  
    Vagas_ocupadas[vaga] = vaga
    cont += 1 
    cont_vga +=1
    print(Vagas_ocupadas)
    while True:
        placa_carro = input('Digite a placa do seu carro: ')
        if placa_carro in Placas:
            print ("Este carro ja está em outra vaga") 
            Vagas_ocupadas[cont] = None
            continue
        elif placa_carro == "":
            print("Está não é uma placa valida")
            continue
        else:
            Placas[vaga] = placa_carro
            cont -= 1
            
            break    
    print (Placas)
    while True:
        saida = input("Você deseja sair do estacionamento(S/N)")
        if "S" in saida.upper():
            while True:
                if  Vagas_ocupadas.size == 0 or not Vagas_ocupadas.any():
                    print("não existe nenhum carro estacionado nesse estacionamento")
                    break
                vaga_estacionada = int(input("Em qual vaga você estava?"))
                if Vagas_ocupadas[vaga_estacionada] == None:
                    print('esta vaga não esta ocupada')
                    continue
                else:
                    Vagas_ocupadas[vaga_estacionada] = None 
                    Placas [vaga_estacionada] = None
                    cont -=1
                    cont_vga -=1
                    print (Vagas_ocupadas)  
                    break
        else:
            break
    while True:
        consulta = input ("Você quer consultar algum veiculo? (S/N)")
        if "S" in consulta.upper():
            while True:
                if  Vagas_ocupadas.size == 0 or not Vagas_ocupadas.any():
                    print("não existe nenhum carro estacionado nesse estacionamento")
                    break
                placa_consulta = input("digite a placa do carro que você quer consultar")
                if placa_consulta in Placas:
                    indice_placa = np.where(Placas == placa_consulta)[0][0]
                    vaga_correspondente = Vagas_ocupadas[indice_placa]
                    if vaga_correspondente in A:
                        setor = "A"
                    elif vaga_correspondente in B:
                        setor = "B"
                    else:
                        setor = "C"
                    print (f"O seu carro com a placa {placa_consulta} está na vaga {vaga_correspondente} no setor {setor}")
                else:
                    print ("Não existe nenhum veiculo com esta placa no estacionamento, verifique se digitou corretamente")
                    continue
        else:
            print("Consulta encerrada.")
            break
