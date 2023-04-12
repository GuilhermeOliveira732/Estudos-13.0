import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

#carregando o arquivo de excel a ser usado como base de dados
df = pd.read_excel(r"C:\Users\guiga\Desktop\pasta\dados.xlsx")

#conferindo os nomes de cada coluna
headers = df.columns.tolist()
print(headers)
print('*'*10)

#conferindo os valores da coluna 3, para saber se batem com os dados que estou procurando
print(df['Unnamed: 3'])
print('*'*10)
#mostrando os 5 itens mais comuns na coluna 3
contagem = df['Unnamed: 3'].value_counts()
tops = contagem.head(5)
print(tops)
print('*'*10)

#limpando e filtrando os dados e adquirindo os dados relativos às vendas do produto "Iron Man G" para o ano de 2019
df = df[['Unnamed: 3', 'Unnamed: 7', 'Unnamed: 9']].dropna()
df = df[df['Unnamed: 9'] != 'Date']
df['Unnamed: 9'] = pd.to_datetime(df['Unnamed: 9'])

df = df[pd.to_datetime(df['Unnamed: 9']).dt.year == 2019]
df = df[df['Unnamed: 3'] == '002d4ea7c04739c130bb74d7e7cd16943']


print(df)

df = df.groupby(['Unnamed: 3', pd.Grouper(key='Unnamed: 9', freq='m')])['Unnamed: 7'].sum().reset_index()
print('Esses dados')

#Gerando o gráfico com os dados adiquiridos anteriormente
for produto in df['Unnamed: 3'].unique():
    dados_produto = df[df['Unnamed: 3'] == produto]
    plt.plot(dados_produto['Unnamed: 9'], dados_produto['Unnamed: 7'], label=produto)

plt.legend()
plt.xlabel('Data')
plt.ylabel('Quantidade vendida')
plt.title('Vendas por produto em 2019')
plt.show()
