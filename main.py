import requests
import pandas as pd
import matplotlib.pyplot as plt

# Definir a URL para API de preços do Bitcoin
url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-02-16&end=2023-02-16'

# Fazer a requisição para a API e obter os dados
response = requests.get(url)
data = response.json()

# Converter os dados para um objeto pandas DataFrame
df = pd.DataFrame.from_dict(data['bpi'], orient='index', columns=['price'])

# Calcular a média móvel de 50 dias
df['MA50'] = df['price'].rolling(window=50).mean()

# Calcular a média móvel de 200 dias
df['MA200'] = df['price'].rolling(window=200).mean()

# Plotar o gráfico com as médias móveis
plt.plot(df['price'])
plt.plot(df['MA50'])
plt.plot(df['MA200'])
plt.legend(['Preço', 'MA50', 'MA200'])
plt.show()