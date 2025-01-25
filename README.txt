Este repositório contém o código e os dados utilizados no projeto de previsão de consumo de energia elétrica. O objetivo do projeto é desenvolver um modelo preditivo que estime o consumo de energia (em kWh) e o gasto associado (em euros), utilizando variáveis como horas de uso de energia, dia da semana, estação do ano, temperatura ambiente e número de pessoas na residência.

Estrutura do Repositório
data/
	energia_consumo.csv      
model/
	energy_model.pkl         
.gitattributes  
data_generation.py
gráfico.py        
predict.py             
README.md                    
train_model.py

Comandos Executados no Desenvolvimento do Projeto

1. Instalação de Dependências
Antes de iniciar qualquer etapa do projeto, instalamos as bibliotecas necessárias.
Comandos executados:
	pip install pandas
	pip install scikit-learn
	pip install joblib
	pip install tkinter
	pip install seaborn
	pip install matplotlib
	pip install random
	pip install datetime


2. Produção de Dados Sintéticos
Para criar o conjunto de dados utilizados no treino do modelo, executamos o script data_generation.py.
Comando executado:

	python src/data_generation.py
Saída:
	Arquivo gerado: data/energia_consumo.csv


3. Análise Exploratória
Realizamos a análise exploratória dos dados com o notebook exploratory_analysis.ipynb.
Comando executado:
	jupyter notebook notebooks/exploratory_analysis.ipynb
A análise incluiu:
	Gráficos de dispersão para relacionar consumo com temperatura.
	Gráficos de barras para consumo médio por estação e faixa de temperatura.
	Histogramas para verificar a distribuição do consumo.

4. Treino do Modelo
O modelo de regressão foi treinado utilizando o script train_model.py, que realiza o pré-processamento dos dados, treino e avaliação do modelo.
Comando executado:
	python src/train_model.py
Saída:
	Métricas exibidas no terminal:
		Erro Médio Absoluto (MAE): 0.72 kWh
		Coeficiente de Determinação (R²): 0.89
Modelo treinado salvo em: model/energy_model.pkl

5. Execução da Interface Gráfica
Criamos uma interface gráfica para previsões em tempo real utilizando o script predict.py.
Comando executado:
	python src/predict.py
Passos realizados na interface:
	Inserção de valores para "Horas de Energia", "Dia da Semana", "Estação", "Temperatura" e "Número de Pessoas".
Clique em Fazer Previsão para calcular o consumo previsto.
6. Validação do Modelo
Realizamos testes adicionais com diferentes subconjuntos de dados para verificar a consistência do modelo.
Comando utilizado para amostragem:
	df.sample(n=200, random_state=42)
Comando para validação manual:
	model.predict(novos_dados)