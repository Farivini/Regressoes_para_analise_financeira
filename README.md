# Regressoes_para_analise_financeira

""" 

Estamos tentando explicar o nivel dos preços das casas 

                MINIMOS QUADRADOS ORDINARIOS
==============================================================================
Dep. Variable:            House Price   R-squared:                       0.678 -> Valor do R quadrado demonstra e siginifica que nossa variave independente
Model:                            OLS   Adj. R-squared:                  0.660     que é o tamanho da casa pode explicar 68% da variavel dependente que é o valor da casa.
Method:                 Least Squares   F-statistic:                     37.95     por ser acima de 30% nosso modelo tem um bom modelo explicativo
Date:                Tue, 06 Oct 2020   Prob (F-statistic):           8.13e-06


const                2.608e+05   9.76e+04      2.673      0.016    5.58e+04    4.66e+05
House Size (sq.ft.)   401.9163     65.243      6.160      0.000     264.846     538.987

Nosso coeficiente 260,800 nossa linha parte do eixo y

A inclinação da linha de regressão beta esta com valor de 401.9 ou 402 
Esse valor pode variar conforme nossa tabela 65 para cima ou para baixo


Pelo resultado da nossa regressão podemos fazer o seguinte calculo
"""

calc_regre = 260800 + 402 * 1000
print(calc_regre)


![Regressão](https://user-images.githubusercontent.com/64615200/95282144-33c58580-082f-11eb-89ac-e00eef857e27.png)
