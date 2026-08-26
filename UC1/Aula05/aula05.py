### ESTRUTURAS DE REPETIÇÃO:

# FOR:
# for i in range(-102,-1,2):
#     print(i)

# WHILE:

# somador = int(input("Registro:"))
# controle = 0

# while controle <= 30:
#     controle=controle+somador
#     somador = int(input("Registro:"))

# print("Oficina lotada!")

# FOR 
acertou = 0
while acertou < 5:
    print(f"Número {acertou + 1} de 5:") 
    num = float(input("Digite um número: ")) 
        
    dobro = num * 2 
    triplo = num * 3 
    quádruplo = num * 4 
        
    print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    acertou+=1 

# DO WHILE:
    
contador = 0 
limite = 5 
 
while True: # Loop infinito garantido para executar pelo menos uma vez 
    if contador >= limite: 
        break # Ponto de DECISÃO: Se o limite for atingido, usamos 'break' para sair 
         
    try: 
        print(f"Número {contador + 1} de {limite}:") 
        num = float(input("Digite um número: ")) 
         
        dobro = num * 2 
        triplo = num * 3 
        quádruplo = num * 4 
         
        print(f"  Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n") 
         
        contador = contador + 1 # Incremento 
         
    except ValueError: 
        print("Entrada inválida. Tente novamente.")
