from validadorCNPJAlfa import validarCNPJ

#Formato válido AA.AAA.AAA/AAAA-DV
#               XI.H9V.M0F/0001-24 = XIH9VM0F000124    
#                                    M77IORS9000140    
#                                    BBWH5FQI000145 
#                                    14691144000146 - Padrão anterior  

validarCNPJ("12.345.678/0001-95")

validarCNPJ("12345678000195")

validarCNPJ("XIH9VM0F000124")

validarCNPJ("BBWH5FQI000145")

validarCNPJ("BBW#5FQI000145")
