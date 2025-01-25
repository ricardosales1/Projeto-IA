import pandas as pd
import numpy as np

# Faixas de temperatura típicas em Portugal para cada estação
faixas_temperatura = {
    "inverno": (0, 15),   # Inverno: 0°C a 15°C
    "primavera": (10, 25),  # Primavera: 10°C a 25°C
    "verão": (20, 35),    # Verão: 20°C a 35°C
    "outono": (10, 20)    # Outono: 10°C a 20°C
}

# Dias da semana
dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

# Gerar amostras por estação
amostras = []
for estacao, (temp_min, temp_max) in faixas_temperatura.items():
    for _ in range(25):  # 25 amostras por estação
        temperatura = round(np.random.uniform(temp_min, temp_max), 1)
        horas_energia = np.random.randint(1, 25)  # Entre 1 e 24 horas
        dia_semana = np.random.choice(dias_semana)
        pessoas = np.random.randint(1, 6)  # Entre 1 e 5 pessoas
        consumo_kwh = round(horas_energia * (0.5 + pessoas * 0.1 + temperatura * 0.05), 2)
        gasto_euros = round(consumo_kwh * 0.15, 2)  # Supor custo de 0.15 euros por kWh
        amostras.append([horas_energia, dia_semana, estacao, temperatura, pessoas, consumo_kwh, gasto_euros])

# Converter para DataFrame
df_amostras = pd.DataFrame(amostras, columns=[
    "horas_energia", "dia_semana", "estacao", "temperatura", "pessoas", "consumo_kwh", "gasto_euros"
])

# Salvar para CSV
df_amostras.to_csv("data/previsao_historico_gerado.csv", index=False)

print("Amostras geradas e salvas em 'data/previsao_historico_gerado.csv'.")
