### LÓGICA E CONDICIONAIS ###
# 1

# cnh = True
# bebidinha = False
#                #True    #True
# posso_dirigir = cnh and not bebidinha
# print(posso_dirigir)


# 2
# busaum = False
# trenzin = False

# venho_pra_aula = busaum or trenzin
# print("Venho pra aula?",venho_pra_aula)

#3

locomocao = input("Diga qual sua locomoção:")
choveu = True

if choveu and locomocao=='moto':
    resultado = "Tô todo molhado :("
elif not choveu and locomocao=='moto':
    resultado = "Tô seco :)"
else:
    resultado = "Tô seco :)"

print(resultado)