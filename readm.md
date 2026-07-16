# Validador de CNPJ Alfanumérico 🏢🔤

Biblioteca para validação do novo formato de **CNPJ Alfanumérico**, desenvolvido pela Receita Federal do Brasil e previsto para implantação em 2026. O projeto aplica a regra oficial de cálculo do Módulo 11, adaptada para suportar caracteres alfanuméricos, realizando a conversão de letras para seus respectivos valores na tabela ASCII antes da verificação.

**Este trabalho também faz parte do meu processo de aprendizado da linguagem, servindo como prática para consolidar conceitos e aplicar técnicas de programação em um caso real.**

## 📌 Sobre o Novo CNPJ

O CNPJ Alfanumérico mantém a estrutura de **14 dígitos**, dividida em três partes:
* **Inscrição:** 8 caracteres alfanuméricos.
* **Filial:** 4 caracteres alfanuméricos.
* **Dígitos Verificadores (DV):** 2 caracteres estritamente numéricos.

## 🧮 Como Funciona a Validação

A lógica de validação segue o algoritmo do **Módulo 11** com pesos de 2 a 9, adaptada para aceitar letras nas primeiras 12 posições:

1. **Conversão Alfanumérica:** Cada letra (A-Z) é convertida para seu valor da tabela ASCII subtraído de 48 (Ex: `A = 17`, `Z = 42`). Números mantêm seu valor original.
2. **Cálculo do DV1:** Multiplica-se os 12 primeiros caracteres pelos pesos `[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]`. O resto da divisão por 11 define o dígito.
3. **Cálculo do DV2:** Inclui-se o DV1 e multiplica-se os 13 caracteres pelos pesos `[6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]`.

Se o resto da divisão for menor que 2, o dígito verificador vira **0**. Caso contrário, subtrai-se o resto de 11 (`11 - resto`).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 
* **Testes:** Testes manuais, utilizando o arquivo app.py como chamador.

