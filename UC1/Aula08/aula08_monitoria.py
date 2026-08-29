## --- 26-08-2026 --- ##

def calculadora_v1(num1,num2,operador="3"):
    # num1=float(input("Digite seu primeiro número:"))
    # num2=float(input("Digite seu segundo número:"))

    # operador=input("Informe a operação desejada entre: 1. adição; 2. subtração; 3. multiplicação e 4. divisão:")

    match operador:
        case "1":
            resultado = num1+num2
        case "2":
            resultado = num1-num2
        case "3":
            resultado = num1*num2
        case "4":
            if num2!=0:
                resultado = num1/num2
            else:
                print(f"Dividiu por Zero. Errou feio. Errou rude!")
        case _ :
            print("Informe um número de operador válido.")
    
    return resultado

calculinho = calculadora_v1(333,555)

print(calculinho)
