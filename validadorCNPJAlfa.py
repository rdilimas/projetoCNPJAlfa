import sys                     
  
def verificarQtdDigitos(cnpj):
    """
    Verifica se a string do CNPJ possui exatamente 14 caracteres.
    """
    qtd_digitos = len(cnpj)

    if qtd_digitos != 14:
       return False
    else:
       return True
       


def validarDigitoVerificador(cnpj):
    """
    Verifica se os dois últimos caracteres do CNPJ são dígitos numéricos. 
    """   
    dv_01 = cnpj[12] ##caractere na posição 13
    dv_02 = cnpj[13] ##caractere na posição 14
    if dv_01.isdigit() and dv_02.isdigit():
        return True
    else:
        return False
    
def conversaoASCII(cnpj):
    """
    Converte cada caractere do CNPJ em um valor numérico.
    Caso o caractere seja um dígito, ele é mantido como está.
    Caso seja uma letra, é convertido para seu valor ASCII e ajustado subtraindo 48.
    """ 
    vlrsConvertidosASCII = []
    for i, char in enumerate(cnpj, start=1):
        if char.isdigit():
        #  print(f"Posição {i}: '{char}' é numérico")
            vlrsConvertidosASCII.append(int(char))
        elif char.isalpha():
        # Transformar o 48 em parametro
        #  print(f"Posição {i}: '{char}' é alfabético, ASCII é {valor_ASCII}")
            vlrsConvertidosASCII.append(ord(char) - 48)
        else:
        #   print(f"Posição {i}: '{char}' é outro caractere (símbolo)")
            raise ValueError("Caractere inválido no CNPJ. O programa será encerrado.")

    return vlrsConvertidosASCII       



    print("CNPJ digitado", cnpj)

def calcularDigVerificador(vlrsConvertidos, dig):
    """
    Calcula o do dígito verificador do CNPJ usando pesos fixos.
    o primeiro dígitos é calculado com base nos 12 primeiros caracteres, 
    e o segundo com base nos 13 primeiros.

    Calcula o dígito verificador do CNPJ.

    Parâmetros:
        vlrsConvertidos: lista com os valores numéricos do CNPJ.
        dig: inteiro que indica qual dígito será calculado:
            1 para o primeiro dígito verificador
            2 para o segundo dígito verificador
    """
    soma = 0
    pesos = [5,4,3,2,9,8,7,6,5,4,3,2]
    if dig == 2:
        pesos = [6] + pesos

    for i, peso in enumerate(pesos):
        produto = (peso * int(vlrsConvertidos[i]))
        soma += int(produto)
        
    resto = soma % 11
    
    # Regra para definir o dígito
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto    
    
    if dig == 1:
       vlrsConvertidos[12] = digito 
    else:
       vlrsConvertidos[13] = digito    

def validarCNPJ(cnpj):
    """
    Função principal que valida o CNPJ Alfa.
    """
    tamanho_is_valido = verificarQtdDigitos(cnpj)
    if tamanho_is_valido:
       dig_eh_numerico = validarDigitoVerificador(cnpj)
       if dig_eh_numerico:
          try:  
              vlrsConvertidos = conversaoASCII(cnpj)
          except ValueError as erro:
                print(f"ERRO!!! CNPJ Inválido - {erro}")
                return   
           
          digVerificadorRecebido = [int(vlrsConvertidos[12]), int(vlrsConvertidos[13])]
        #   print("Valores convertidos ", vlrsConvertidos)
          calcularDigVerificador(vlrsConvertidos, 1)
          calcularDigVerificador(vlrsConvertidos, 2)
          if (vlrsConvertidos[12:14] == digVerificadorRecebido):
              print("CNPJ Válido!")
          else:
              print("CNPJ Inválido - Digito verificador incorreto!")    
       else:
          print("CNPJ Inválido - Digito não numérico!")   
    else:
       print("CNPJ Inválido - Quantidade de caracteres incorreta!")      
