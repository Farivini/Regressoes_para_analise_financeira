import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt



data = pd.read_excel('Housing.xlsx')
print(data)
#data['House Price','House Size (sq.ft.)']

x = data['House Size (sq.ft.)']
y = data['House Price']

print(y)
print(x)

plt.scatter(x,y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('Preço das casas')
plt.xlabel('Tamanho das casas')
plt.show()

"""
Vamos colocar uma constante
 
Redefinimos o X para X1

fit aplica uma tecnica de estimativa especifica

"""
x1 = sm.add_constant(x)
regress = sm.OLS(y, x1).fit()
print(regress.summary())

""" 

Estamos tentando explicar o nivel dos preços das casas 

                MINIMOS QUADRADOS ORDINARIOS
==============================================================================
Dep. Variable:            House Price   R-squared:                       0.678 -> Valor do R quadrado demonstra e siginifica que nossa variave independente
Model:                            OLS   Adj. R-squared:                  0.660    que é o tamanho da casa pode explicar 68% da variavel dependente que é o valor da casa.
Method:                 Least Squares   F-statistic:                     37.95    por ser acima de 30% nosso modelo tem um bom modelo explicativo
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

"""  Vimos no grafico que existem duas casas de 1 mil metros quadrados daquela que previamos 

                ALPHA ------------- BETA --------------- R^2

"""
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(slope)
print(intercept)
print(r_value)
print(p_value)
print(std_err)
