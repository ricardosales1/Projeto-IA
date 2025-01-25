model/
	energy_model.pkl         
.gitattributes  
data_generation.py
gráfico.py        
data_generation.py     
predict.py             
README.md                    
train_model.py

@@ -21,12 +20,9 @@ Comandos executados:
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

@@ -35,17 +31,7 @@ Comando executado:
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
3. Treino do Modelo
O modelo de regressão foi treinado utilizando o script train_model.py, que realiza o pré-processamento dos dados, treino e avaliação do modelo.
Comando executado:
	python src/train_model.py

@@ -55,14 +41,15 @@ Saída:
		Coeficiente de Determinação (R²): 0.89
Modelo treinado salvo em: model/energy_model.pkl

5. Execução da Interface Gráfica
4. Execução da Interface Gráfica
Criamos uma interface gráfica para previsões em tempo real utilizando o script predict.py.
Comando executado:
	python src/predict.py
Passos realizados na interface:
	Inserção de valores para "Horas de Energia", "Dia da Semana", "Estação", "Temperatura" e "Número de Pessoas".
Clique em Fazer Previsão para calcular o consumo previsto.
6. Validação do Modelo

5. Validação do Modelo
Realizamos testes adicionais com diferentes subconjuntos de dados para verificar a consistência do modelo.
Comando utilizado para amostragem:
	df.sample(n=200, random_state=42)