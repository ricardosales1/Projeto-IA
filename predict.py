import joblib
import pandas as pd

# Carregar o modelo salvo
model = joblib.load('model/energy_model.pkl')

# Listas de valores válidos
dias_semana_validos = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
estacoes_validas = ['inverno', 'primavera', 'verão', 'outono']

# Função para obter e validar entrada do usuário
def obter_dados_usuario():
    print("Por favor, insira os dados para previsão:")

    # Validar horas de energia (deve ser um número inteiro positivo)
    while True:
        try:
            horas_energia = int(input("Horas de energia utilizadas (0 a 24): "))
            if 0 <= horas_energia <= 24:
                break
            else:
                print("Por favor, insira um número entre 0 e 24.")
        except ValueError:
            print("Entrada inválida! Insira um número inteiro.")

    # Validar dia da semana
    while True:
        dia_semana = input("Dia da semana (segunda, terça, ..., domingo): ").lower()
        if dia_semana in dias_semana_validos:
            break
        else:
            print(f"Entrada inválida! Escolha entre: {', '.join(dias_semana_validos)}.")

    # Validar estação do ano
    while True:
        estacao = input("Estação do ano (inverno, primavera, verão, outono): ").lower()
        if estacao in estacoes_validas:
            break
        else:
            print(f"Entrada inválida! Escolha entre: {', '.join(estacoes_validas)}.")

    # Validar temperatura (deve ser um número)
    while True:
        try:
            temperatura = float(input("Temperatura (em °C, ex.: 25.5): "))
            break
        except ValueError:
            print("Entrada inválida! Insira um número válido para a temperatura.")

    # Validar número de pessoas (deve ser um número inteiro positivo)
    while True:
        try:
            pessoas = int(input("Número de pessoas (1 a 10): "))
            if 1 <= pessoas <= 10:
                break
            else:
                print("Por favor, insira um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida! Insira um número inteiro.")

    return {
        'horas_energia': [horas_energia],
        'dia_semana': [dia_semana],
        'estacao': [estacao],
        'temperatura': [temperatura],
        'pessoas': [pessoas]
    }

# Obter os dados do usuário
dados_usuario = obter_dados_usuario()

# Criar DataFrame com os dados do usuário
novos_dados = pd.DataFrame(dados_usuario)

# Fazer previsão
previsao = model.predict(novos_dados)
novos_dados['consumo_previsto_kwh'] = previsao

# Exibir os resultados
print("\nPrevisão de Consumo de Energia:")
print(novos_dados)