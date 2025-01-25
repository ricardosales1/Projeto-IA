import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib
from tkinter import PhotoImage

# Carregar o modelo salvo
model = joblib.load('model/energy_model.pkl')

def calcular_gasto(consumo_kwh):
    tarifa = 0.15  # Euros por kWh
    return consumo_kwh * tarifa

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

        # Exibir os resultados
        resultado_label.config(text=f"Consumo Previsto: {previsao[0]:.2f} kWh")
        custo_label.config(text=f"Custo Estimado: €{custo:.2f}")

    except ValueError as e:
        messagebox.showerror("Erro de Validação", f"Entrada inválida: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Previsão de Consumo de Energia")
janela.geometry("400x500")  # Ajustando o tamanho da janela
janela.config(bg="#f0f0f0")  # Cor de fundo

# Adicionar logo
logo = PhotoImage(file="logo.png")  # Substitua pelo caminho correto da sua logo
logo_label = tk.Label(janela, image=logo, bg="#f0f0f0")
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Criar os widgets com mais estilo
# Horas de energia
tk.Label(janela, text="Horas de energia (0-24):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=10)
entry_horas_energia = tk.Entry(janela, font=("Helvetica", 12))
entry_horas_energia.grid(row=1, column=1, padx=10, pady=5)

# Dia da semana
tk.Label(janela, text="Dia da semana:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=10)
dia_semana_var = tk.StringVar(value="segunda")
dia_semana_menu = tk.OptionMenu(janela, dia_semana_var, "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
dia_semana_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Estação do ano
tk.Label(janela, text="Estação do ano:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=10)
estacao_var = tk.StringVar(value="inverno")
estacao_menu = tk.OptionMenu(janela, estacao_var, "inverno", "primavera", "verão", "outono")
estacao_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Temperatura
tk.Label(janela, text="Temperatura (°C):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=4, column=0, sticky="w", padx=10)
entry_temperatura = tk.Entry(janela, font=("Helvetica", 12))
entry_temperatura.grid(row=4, column=1, padx=10, pady=5)

# Número de pessoas
tk.Label(janela, text="Número de pessoas (1-10):", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=5, column=0, sticky="w", padx=10)
entry_pessoas = tk.Entry(janela, font=("Helvetica", 12))
entry_pessoas.grid(row=5, column=1, padx=10, pady=5)

# Botão para fazer previsão
btn_prever = tk.Button(janela, text="Fazer Previsão", command=fazer_previsao, bg="#0076a3", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=2)
btn_prever.grid(row=6, column=0, columnspan=2, pady=20)

# Label para exibir o resultado do consumo
resultado_label = tk.Label(janela, text="", bg="#f0f0f0", font=("Helvetica", 14, "bold"))
resultado_label.grid(row=7, column=0, columnspan=2)

# Label para exibir o custo estimado
custo_label = tk.Label(janela, text="", bg="#f0f0f0", font=("Helvetica", 14, "bold"))
custo_label.grid(row=8, column=0, columnspan=2)

# Iniciar o loop principal da interface
janela.mainloop()