mes = int(input("Informe o mês de seu nascimento:"))

# # VISÃO IF/ELSE:
# if mes==1:
#     signo="Aquário"
# elif mes==2:
#     signo="Peixes"
# elif mes==3:
#     signo="Áries"
# elif mes==4:
#     signo="Touro"
# elif mes==5:
#     signo="Gêmeos"
# elif mes==6:
#     signo="Câncer"
# elif mes==7:
#     signo="Leão"
# elif mes==8:
#     signo="Virgem"
# elif mes==9:
#     signo="Libra"
# elif mes==10:
#     signo="Escorpião"
# elif mes==11:
#     signo="Sagitário"
# else:
#     signo="Capricórnio"

# print(f"Seu signo é {signo}.")

#VISÃO MATCH CASE:
match mes:
    case 1:
        signo="Aquário"
    case 2:
        signo="Áries"
    case 3:
        signo="Touro"
    case 4:
        signo="Gêmeos"
    case 5:
        signo="Câncer"
    case _:
        signo="Número de mês inválido"

print(f"{signo}.")
    

