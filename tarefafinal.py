import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.prada.com/br/pt/womens/bags/c/10062BR'
resposta = requests.get(url, verify=False)
sopa = BeautifulSoup(resposta.text, 'html.parser')

lista_bolsas = []
texto_nomes = sopa.find_all('h3', class_='product-card__name')
for nome in texto_nomes:
    lista_bolsas.append(nome.text.strip())

lista_valores = []
texto_precos = sopa.find_all('p', class_='product-card__price--new')
for preco in texto_precos:
    lista_valores.append(preco.text.strip())

dicionario = {'Bolsas': lista_bolsas, 'Valor': lista_valores}
dataframe = pd.DataFrame(dicionario)

plt.figure(figsize=(10, 6))
plt.barh(dataframe['Bolsas'], dataframe['Valor'], color='skyblue')
plt.xlabel('Preço (R$)')
plt.ylabel('Modelo de Bolsa')
plt.title('Preços das Bolsas da Prada')
plt.gca().invert_yaxis() 
plt.tight_layout()

plt.show()