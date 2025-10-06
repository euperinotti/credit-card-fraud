import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregue o dataset
# Certifique-se de que o nome do arquivo corresponde ao que você tem
file_path = 'creditcard.csv'
df = pd.read_csv(file_path)

# --- 1. Inspeção Inicial dos Dados ---
print("--- Visão Geral dos Dados ---")
print(df.head())
print("\n--- Informações do Dataset ---")
df.info()
print("\n--- Estatísticas Descritivas ---")
print(df.describe())

# --- 2. Análise da Variável Alvo (Class) ---
print("\n--- Contagem de Classes (0: Não Fraude, 1: Fraude) ---")
print(df['Class'].value_counts())
print("\n--- Proporção de Classes (%) ---")
print(df['Class'].value_counts(normalize=True) * 100)

plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=df)
plt.title('Distribuição das Classes (0: Não Fraude, 1: Fraude)')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.xticks([0, 1], ['Não Fraude', 'Fraude'])
plt.savefig('class_distribution.png')
plt.show()

# --- 3. Análise das Features 'Time' e 'Amount' ---
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(df['Time'], bins=50, kde=True)
plt.title('Distribuição do Tempo de Transação')
plt.xlabel('Tempo (segundos)')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title('Distribuição do Valor da Transação')
plt.xlabel('Valor (Amount)')
plt.ylabel('Frequência')
plt.xlim(0, 5000) # Limita o eixo x para melhor visualização

plt.tight_layout()
plt.savefig('time_amount_distribution.png')
plt.show()

# --- 4. Matriz de Correlação ---
corr = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap='coolwarm', annot=False)
plt.title('Matriz de Correlação das Features')
plt.savefig('correlation_matrix.png')
plt.show()