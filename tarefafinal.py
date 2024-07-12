import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup
import streamlit as st
from reportlab.pdfgen import canvas
import os
import pypdf
from pathlib import Path

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

st.title('Gráfico da Prada')
st.markdown('Se você ama moda tanto quanto nós, vai adorar conferir os novos modelos das bolsas da Prada no nosso gráfico super detalhado.')
st.markdown('Variedade de Modelos: Desde clutches delicadas até tote bags espaçosas, há uma bolsa Prada para cada ocasião. Qualidade Superior: Feitas com os melhores materiais e artesanato de alta qualidade. Design Inovador: Sempre na vanguarda da moda, as bolsas Prada são icônicas e atemporais.')
st.pyplot(plt.gcf())

botao = st.button('Salvar PDF')
   
pasta = 'paginas'
if not os.path.exists(pasta):
    os.makedirs(pasta)

arquivo_pdf = pypdf.PdfReader('MGLU_ER_3T20_POR.pdf')

i = 1
for pagina in arquivo_pdf.pages:
    arquivo_novo = pypdf.PdfWriter()
    arquivo_novo.add_page(pagina)

with Path(f'paginas/Pagina{i}.pdf').open(mode='wb') as arquivo_final:
        arquivo_novo.write(arquivo_final)
        i += 1
