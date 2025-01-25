import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Carregar os dados do histórico de previsões
try:
    df = pd.read_csv('data/previsao_historico.csv')
except FileNotFoundError:
    raise FileNotFoundError("O arquivo 'data/previsao_historico.csv' não foi encontrado.")

# Determinar o número máximo de amostras disponíveis e selecionar amostras aleatórias para clareza
n_amostras = min(len(df), 200)
amostras = df.sample(n=n_amostras, random_state=42)

def create_figures():
    """Cria e retorna os gráficos em uma lista."""
    figures = []

    # **1. Gráfico de Dispersão (Temperatura x Consumo)**
    fig1 = plt.figure(figsize=(8, 6))
    plt.scatter(amostras['temperatura'], amostras['consumo_kwh'], alpha=0.6, color='blue')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Consumo de Energia Previsto (kWh)')
    plt.title('Relação entre Temperatura e Consumo de Energia Previsto')
    plt.grid()
    figures.append(fig1)

    # **2. Gráfico de Barras (Consumo Médio por Faixa de Temperatura)**
    df['faixa_temp'] = pd.cut(df['temperatura'], bins=10)
    agrupado = df.groupby('faixa_temp')['consumo_kwh'].mean()

    fig2 = plt.figure(figsize=(10, 6))
    agrupado.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.xlabel('Faixa de Temperatura (°C)')
    plt.ylabel('Consumo Médio de Energia Previsto (kWh)')
    plt.title('Consumo Médio de Energia Previsto por Faixa de Temperatura')
    plt.grid(axis='y')
    figures.append(fig2)

    # **3. Gráfico de Dispersão Colorido por Estação**
    fig3 = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=amostras, x='temperatura', y='consumo_kwh', hue='estacao', palette='Set2', alpha=0.7)
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Consumo de Energia Previsto (kWh)')
    plt.title('Relação entre Temperatura e Consumo de Energia Previsto por Estação')
    plt.grid()
    figures.append(fig3)

    # **4. Histograma (Distribuição do Consumo de Energia Previsto)**
    fig4 = plt.figure(figsize=(8, 6))
    df['consumo_kwh'].plot(kind='hist', bins=20, color='coral', edgecolor='black', alpha=0.7)
    plt.xlabel('Consumo de Energia Previsto (kWh)')
    plt.ylabel('Frequência')
    plt.title('Distribuição do Consumo de Energia Previsto')
    plt.grid(axis='y')
    figures.append(fig4)

    # **5. Boxplot (Consumo por Estação do Ano)**
    fig5 = plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='estacao', y='consumo_kwh', palette='coolwarm')
    plt.xlabel('Estação do Ano')
    plt.ylabel('Consumo de Energia Previsto (kWh)')
    plt.title('Consumo de Energia Previsto por Estação do Ano')
    plt.grid(axis='y')
    figures.append(fig5)

    return figures

def show_figure(index):
    """Exibe o gráfico com base no índice fornecido."""
    global canvas

    if canvas:
        canvas.get_tk_widget().pack_forget()

    figure = figures[index]
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def next_figure():
    """Mostra o próximo gráfico."""
    global current_index
    if current_index < len(figures) - 1:
        current_index += 1
        show_figure(current_index)

def prev_figure():
    """Mostra o gráfico anterior.""" 
    global current_index
    if current_index > 0:
        current_index -= 1
        show_figure(current_index)

def voltar():
    """Fecha a janela do Tkinter quando o botão 'Voltar' é pressionado."""
    root.destroy()

# Criar a janela do Tkinter
root = tk.Tk()
root.title("Navegador de Gráficos")
root.geometry("900x700")

# Criar os gráficos
figures = create_figures()
current_index = 0
canvas = None

# Exibir o primeiro gráfico
show_figure(current_index)

# Adicionar um frame na parte inferior para os botões
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Adicionar os botões dentro do frame
btn_prev = tk.Button(button_frame, text="Anterior", command=prev_figure)
btn_prev.pack(side=tk.LEFT, padx=10)

btn_next = tk.Button(button_frame, text="Próximo", command=next_figure)
btn_next.pack(side=tk.RIGHT, padx=10)

# Adicionar o botão "Voltar" com a cor #FF6F61
btn_voltar = tk.Button(button_frame, text="Voltar", command=voltar, bg="#FF6F61", fg="white")
btn_voltar.pack(side=tk.BOTTOM, pady=5)

# Iniciar o loop principal do Tkinter
root.mainloop()
