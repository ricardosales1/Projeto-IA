import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import joblib
from tkinter import PhotoImage
import os
import subprocess

# Carregar o modelo salvo
model = joblib.load('model/energy_model.pkl')

# Caminho do ficheiro de histórico de previsões
historico_path = 'data/previsao_historico.csv'

# Função para calcular o gasto em euros
def calcular_gasto(consumo_kwh):
    tarifa = 0.15  # Euros por kWh
    return consumo_kwh * tarifa

# Função para salvar previsão no histórico de previsões
def salvar_historico(horas_energia, dia_semana, estacao, temperatura, pessoas, consumo, custo):
    nova_linha = {
        'horas_energia': horas_energia,
        'dia_semana': dia_semana,
        'estacao': estacao,
        'temperatura': temperatura,
        'pessoas': pessoas,
        'consumo_kwh': consumo,
        'gasto_euros': custo
    }

    if not os.path.exists(historico_path):
        df = pd.DataFrame([nova_linha])
        df.to_csv(historico_path, index=False)
    else:
        df = pd.read_csv(historico_path)
        df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
        df.to_csv(historico_path, index=False)

# Função para fazer previsão
def fazer_previsao():
    try:
        # Obter os valores inseridos pelo usuário
        horas_energia = int(entry_horas_energia.get())
        dia_semana = dia_semana_var.get()
        estacao = estacao_var.get()
        temperatura = float(entry_temperatura.get())
        pessoas = int(entry_pessoas.get())

        # Validar os valores
        if not (0 <= horas_energia <= 24):
            raise ValueError("As horas de energia devem estar entre 0 e 24.")
        if not (1 <= pessoas <= 10):
            raise ValueError("O número de pessoas deve estar entre 1 e 10.")

        # Criar DataFrame com os dados do usuário
        novos_dados = pd.DataFrame({
            'horas_energia': [horas_energia],
            'dia_semana': [dia_semana],
            'estacao': [estacao],
            'temperatura': [temperatura],
            'pessoas': [pessoas]
        })

        # Fazer a previsão
        previsao = model.predict(novos_dados)

        # Calcular o custo em euros
        custo = calcular_gasto(previsao[0])

        # Salvar no histórico de previsões
        salvar_historico(horas_energia, dia_semana, estacao, temperatura, pessoas, previsao[0], custo)

        # Exibir os resultados
        resultado_label.config(text=f"Consumo Previsto: {previsao[0]:.2f} kWh")
        custo_label.config(text=f"Custo Estimado: €{custo:.2f}")

    except ValueError as e:
        messagebox.showerror("Erro de Validação", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para abrir o histórico de previsões
def abrir_historico():
    global historico_janela
    janela.destroy()  # Fechar a janela principal

    historico_janela = tk.Tk()
    historico_janela.title("Histórico de Previsões")

    # Verificar se o histórico existe
    if not os.path.exists(historico_path):
        messagebox.showerror("Erro", "O arquivo de histórico não foi encontrado.")
        historico_janela.destroy()
        return

    # Ler o arquivo CSV
    df = pd.read_csv(historico_path)

    # Ajustar o tamanho da janela para caber o conteúdo
    largura = max(700, 100 * len(df.columns))
    altura = 400
    historico_janela.geometry(f"{largura}x{altura}")

    # Criar tabela
    tabela = ttk.Treeview(historico_janela, columns=list(df.columns), show='headings')
    tabela.pack(expand=True, fill='both')

    # Configurar cabeçalhos
    for coluna in df.columns:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, anchor='center', width=100)

    # Adicionar os dados na tabela
    for _, linha in df.iterrows():
        tabela.insert('', 'end', values=list(linha))

    # Barra de rolagem
    scrollbar = ttk.Scrollbar(historico_janela, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

    # Botão para voltar
    btn_voltar = tk.Button(historico_janela, text="Voltar", command=voltar_para_previsao, bg="#FF6F61", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
    btn_voltar.pack(pady=10, side='left', padx=10)

    # Botão para abrir gráficos
    btn_graficos = tk.Button(historico_janela, text="Abrir Gráficos", command=abrir_graficos, bg="#0076a3", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
    btn_graficos.pack(pady=10, side='left', padx=10)

# Função para abrir os gráficos do grafico.py
def abrir_graficos():
    try:
        subprocess.Popen(['python', 'grafico.py'])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir os gráficos: {e}")

# Função para voltar à janela principal
def voltar_para_previsao():
    historico_janela.destroy()
    criar_janela_principal()

# Função para criar a janela principal
def criar_janela_principal():
    global janela, entry_horas_energia, dia_semana_var, estacao_var, entry_temperatura, entry_pessoas, resultado_label, custo_label

    janela = tk.Tk()
    janela.title("Previsão de Consumo de Energia")
    janela.geometry("440x500")
    janela.config(bg="#f0f0f0")

    # Adicionar logo
    logo = PhotoImage(file="logo.png")  # Substitua pelo caminho correto da sua logo
    logo_label = tk.Label(janela, image=logo, bg="#f0f0f0")
    logo_label.image = logo
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Criar os widgets
    tk.Label(janela, text="Horas de energia (0-24):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=10)
    entry_horas_energia = tk.Entry(janela, font=("Helvetica", 12))
    entry_horas_energia.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela, text="Dia da semana:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=10)
    dia_semana_var = tk.StringVar(value="segunda")
    dia_semana_menu = tk.OptionMenu(janela, dia_semana_var, "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
    dia_semana_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    tk.Label(janela, text="Estação do ano:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=10)
    estacao_var = tk.StringVar(value="inverno")
    estacao_menu = tk.OptionMenu(janela, estacao_var, "inverno", "primavera", "verão", "outono")
    estacao_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    tk.Label(janela, text="Temperatura (°C):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=10)
    entry_temperatura = tk.Entry(janela, font=("Helvetica", 12))
    entry_temperatura.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(janela, text="Número de pessoas (1-10):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=10)
    entry_pessoas = tk.Entry(janela, font=("Helvetica", 12))
    entry_pessoas.grid(row=5, column=1, padx=10, pady=5)

    btn_prever = tk.Button(janela, text="Fazer Previsão", command=fazer_previsao, bg="#0076a3", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
    btn_prever.grid(row=6, column=0, pady=20, padx=10, sticky="e")

    btn_historico = tk.Button(janela, text="Histórico de Previsões", command=abrir_historico, bg="#0076a3", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
    btn_historico.grid(row=6, column=1, pady=20, padx=10, sticky="w")

    resultado_label = tk.Label(janela, text="", bg="#f0f0f0", font=("Helvetica", 14, "bold"))
    resultado_label.grid(row=7, column=0, columnspan=2)

    custo_label = tk.Label(janela, text="", bg="#f0f0f0", font=("Helvetica", 14, "bold"))
    custo_label.grid(row=8, column=0, columnspan=2)

    janela.mainloop()

# Inicializar a aplicação
criar_janela_principal()
