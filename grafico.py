# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('data/energia_consumo.csv')

# Reduzir o número de amostras para clareza (opcional)
amostras = df.sample(n=200, random_state=42)  # Escolhendo 200 amostras aleatórias

# **1. Gráfico de Dispersão (Temperatura x Consumo)**
plt.figure(figsize=(8, 6))
plt.scatter(amostras['temperatura'], amostras['consumo_kwh'], alpha=0.6, color='blue')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Consumo de Energia (kWh)')
plt.title('Relação entre Temperatura e Consumo de Energia (200 Amostras)')
plt.grid()
plt.show()

# **2. Gráfico de Barras (Consumo Médio por Faixa de Temperatura)**
# Criar faixas de temperatura e calcular média de consumo
df['faixa_temp'] = pd.cut(df['temperatura'], bins=10)
agrupado = df.groupby('faixa_temp')['consumo_kwh'].mean()

plt.figure(figsize=(10, 6))
agrupado.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Faixa de Temperatura (°C)')
plt.ylabel('Consumo Médio de Energia (kWh)')
plt.title('Consumo Médio de Energia por Faixa de Temperatura')
plt.grid(axis='y')
plt.show()

# **3. Gráfico de Dispersão Colorido por Estação**
plt.figure(figsize=(8, 6))
sns.scatterplot(data=amostras, x='temperatura', y='consumo_kwh', hue='estacao', palette='Set2', alpha=0.7)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Consumo de Energia (kWh)')
plt.title('Relação entre Temperatura e Consumo de Energia por Estação')
plt.grid()
plt.show()

# **4. Histograma (Distribuição do Consumo de Energia)**
plt.figure(figsize=(8, 6))
df['consumo_kwh'].plot(kind='hist', bins=20, color='coral', edgecolor='black', alpha=0.7)
plt.xlabel('Consumo de Energia (kWh)')
plt.ylabel('Frequência')
plt.title('Distribuição do Consumo de Energia')
plt.grid(axis='y')
plt.show()

# **5. Boxplot (Consumo por Estação do Ano)**
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='estacao', y='consumo_kwh', palette='coolwarm')
plt.xlabel('Estação do Ano')
plt.ylabel('Consumo de Energia (kWh)')
plt.title('Consumo de Energia por Estação do Ano')
plt.grid(axis='y')
plt.show()
