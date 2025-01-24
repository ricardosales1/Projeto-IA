import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_horas_energia():
    return random.randint(0, 24)

def gerar_dia_da_semana():
    return random.choice(['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'])

def determinar_estacao(data_criacao):
    mes = data_criacao.month
    if mes in [12, 1, 2]:
        return 'inverno'
    elif mes in [3, 4, 5]:
        return 'primavera'
    elif mes in [6, 7, 8]:
        return 'verão'
    elif mes in [9, 10, 11]:
        return 'outono'

def gerar_temperatura(horas_energia, dia_semana, estacao):
    base_temp = {'inverno': 5, 'primavera': 15, 'verão': 25, 'outono': 10}
    return base_temp[estacao] + random.uniform(-5, 5)

def gerar_pessoas():
    return random.randint(1, 5)

def calcular_consumo(horas_energia, temperatura, pessoas, estacao):
    fator_estacao = {'inverno': 1.2, 'primavera': 1.0, 'verão': 0.8, 'outono': 1.1}
    return (horas_energia * pessoas * fator_estacao[estacao] * (1 + temperatura / 30))

def calcular_gasto(consumo_kwh):
    tarifa = 0.15  # Euros por kWh
    return consumo_kwh * tarifa

def gerar_dados(num_amostras=1000):
    dados = []
    for _ in range(num_amostras):
        data_criacao = datetime(2024, 1, 1) + timedelta(minutes=random.randint(0, 365 * 24 * 60))
        horas_energia = gerar_horas_energia()
        dia_semana = gerar_dia_da_semana()
        estacao = determinar_estacao(data_criacao)
        temperatura = gerar_temperatura(horas_energia, dia_semana, estacao)
        pessoas = gerar_pessoas()
        consumo_kwh = calcular_consumo(horas_energia, temperatura, pessoas, estacao)
        gasto_euros = calcular_gasto(consumo_kwh)
        dados.append([data_criacao, horas_energia, dia_semana, estacao, temperatura, pessoas, consumo_kwh, gasto_euros])

    df = pd.DataFrame(dados, columns=[
        'data_criacao', 'horas_energia', 'dia_semana', 'estacao', 
        'temperatura', 'pessoas', 'consumo_kwh', 'gasto_euros'
    ])
    return df

if __name__ == "__main__":
    df = gerar_dados()
    df.to_csv('data/energia_consumo.csv', index=False)
    print("Dados gerados e salvos em data/energia_consumo.csv")
