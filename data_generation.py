import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar aleatoriamente o número de horas de uso de energia em um dia.
def gerar_horas_energia():
    return random.randint(0, 24)

# Função para escolher aleatoriamente um dia da semana.
def gerar_dia_da_semana():
    return random.choice(['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'])

# Função para determinar a estação do ano com base no mês da data fornecida.
def determinar_estacao(data_criacao):
    mes = data_criacao.month
    if mes in [12, 1, 2]:  # Meses de inverno
        return 'inverno'
    elif mes in [3, 4, 5]:  # Meses de primavera
        return 'primavera'
    elif mes in [6, 7, 8]:  # Meses de verão
        return 'verão'
    elif mes in [9, 10, 11]:  # Meses de outono
        return 'outono'

# Função para calcular uma temperatura média baseada na estação e ajustar com uma variação aleatória.
def gerar_temperatura(horas_energia, dia_semana, estacao):
    base_temp = {'inverno': 5, 'primavera': 15, 'verão': 25, 'outono': 10}
    # Ajuste aleatório para simular flutuações na temperatura.
    return base_temp[estacao] + random.uniform(-5, 5)

# Função para gerar aleatoriamente o número de pessoas consumindo energia.
def gerar_pessoas():
    return random.randint(1, 5)

# Função para calcular o consumo de energia com base em múltiplos fatores.
def calcular_consumo(horas_energia, temperatura, pessoas, estacao):
    fator_estacao = {'inverno': 1.2, 'primavera': 1.0, 'verão': 0.8, 'outono': 1.1}
    # Consumo é influenciado pelas horas de energia, número de pessoas, estação e temperatura.
    return (horas_energia * pessoas * fator_estacao[estacao] * (1 + temperatura / 30))

# Função para calcular o custo em euros com base no consumo de energia em kWh.
def calcular_gasto(consumo_kwh):
    tarifa = 0.15  # Tarifa de energia em euros por kWh.
    return consumo_kwh * tarifa

# Função principal para gerar os dados e organizá-los em um DataFrame.
def gerar_dados(num_amostras=1000):
    dados = []  # Lista para armazenar as amostras geradas.
    for _ in range(num_amostras):
        # Geração de uma data aleatória dentro do ano de 2024.
        data_criacao = datetime(2024, 1, 1) + timedelta(minutes=random.randint(0, 365 * 24 * 60))
        horas_energia = gerar_horas_energia()  # Quantidade de horas de uso de energia.
        dia_semana = gerar_dia_da_semana()  # Dia da semana.
        estacao = determinar_estacao(data_criacao)  # Estação do ano.
        temperatura = gerar_temperatura(horas_energia, dia_semana, estacao)  # Temperatura média.
        pessoas = gerar_pessoas()  # Número de pessoas na residência.
        consumo_kwh = calcular_consumo(horas_energia, temperatura, pessoas, estacao)  # Consumo de energia.
        gasto_euros = calcular_gasto(consumo_kwh)  # Gasto em euros com energia.

        # Adiciona os dados da amostra à lista.
        dados.append([data_criacao, horas_energia, dia_semana, estacao, temperatura, pessoas, consumo_kwh, gasto_euros])

    # Criação de um DataFrame para organizar os dados.
    df = pd.DataFrame(dados, columns=[
        'data_criacao', 'horas_energia', 'dia_semana', 'estacao', 
        'temperatura', 'pessoas', 'consumo_kwh', 'gasto_euros'
    ])
    return df

# Execução principal do script para gerar e salvar os dados em um arquivo CSV.
if __name__ == "__main__":
    df = gerar_dados()  # Gera o DataFrame com os dados simulados.
    df.to_csv('data/energia_consumo.csv', index=False)  # Salva o DataFrame em um arquivo CSV.
    print("Dados gerados e salvos em data/energia_consumo.csv")
