import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Carregar os dados
df = pd.read_csv('data/energia_consumo.csv')

# Dividir variáveis em features (X) e target (y)
X = df[['horas_energia', 'dia_semana', 'estacao', 'temperatura', 'pessoas']]
y = df['consumo_kwh']

# Separar em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pré-processamento: transformar variáveis categóricas em one-hot encoding
categorical_features = ['dia_semana', 'estacao']
categorical_transformer = OneHotEncoder()

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='passthrough'  # Deixar as outras variáveis como estão
)

# Criar pipeline com pré-processamento e modelo
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=4, random_state=42))
])

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Erro Médio Absoluto (MAE): {mae:.2f} kWh")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")

# Salvar o modelo treinado
joblib.dump(model, 'model/energy_model.pkl')
print("Modelo treinado e salvo em model/energy_model.pkl")
