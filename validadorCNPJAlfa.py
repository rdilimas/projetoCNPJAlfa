#Formato válido AA.AAA.AAA/AAAA-DV
#               XI.H9V.M0F/0001-24 = XIH9VM0F000124             
cnpj = 'XIH9VM0F000124' ##  input("Digite seu CNPJ: ")


def verificarQtdDigitos(cnpj):
    qtd_digitos = len(cnpj)
    if qtd_digitos != 14:
       print("CNPJ Inválido!")

def validarDigitoVerificador(cnpj):
    dv_01 = cnpj[12] ##caractere na posição 13
    dv_02 = cnpj[13] ##caractere na posição 14
    if dv_01.isdigit() and dv_02.isdigit():
        print("Digito numérico")
    else:
        print("Digito não numérico")
    
def conversaoASCII(cnpj):
    vlrsConvertidosASCII = []
    for i, char in enumerate(cnpj, start=1):
        if char.isdigit():
            print(f"Posição {i}: '{char}' é numérico")
            vlrsConvertidosASCII.append(char)
        elif char.isalpha():
            valor_ASCII = ord(char)
            valor_ASCII = valor_ASCII - 48 ## Transformar o 48 em parametro
            print(f"Posição {i}: '{char}' é alfabético, ASCII é {valor_ASCII}")
            vlrsConvertidosASCII.append(valor_ASCII)
        else:
            print(f"Posição {i}: '{char}' é outro caractere (símbolo)")

    return vlrsConvertidosASCII       



    print("CNPJ digitado", cnpj)

def calcularPrimDig(vlrsConvertidos):
    soma = 0
    pesos = [5,4,3,2,9,8,7,6,5,4,3,2]
    for i, peso in enumerate(pesos):
        produto = (peso * int(vlrsConvertidos[i]))
        soma += int(produto)
        
        resto = soma % 11
    
    # Regra para definir o dígito
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto    
    
    print("Digito: ", digito )


verificarQtdDigitos(cnpj)
validarDigitoVerificador(cnpj)
vlrsConvertidos = conversaoASCII(cnpj)
print("Valores convertidos ", vlrsConvertidos)
calcularPrimDig(vlrsConvertidos)