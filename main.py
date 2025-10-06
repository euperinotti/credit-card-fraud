# %% [markdown]
# # Análise Exploratória de Dados - Fraude de Cartão de Crédito
#
# ## 1. Carregando as bibliotecas e os dados

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', None)
pd.options.display.float_format = '{:.4f}'.format

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 7)

df = pd.read_csv('creditcard.csv')
# %% [markdown]
# ## 2. Inspeção Inicial e Estatísticas

# %% [markdown]
# ## Head
df.head()
# ## Info & Null Values
df.info()
df.isnull().sum()

# %%
# count: Número de entradas não nulas
# mean: Média
# std: Desvio padrão
# min: Valor mínimo
# 25%: Primeiro quartil (Q1)
# 50%: Mediana (Q2)
# 75%: Terceiro quartil (Q3)
# max: Valor máximo
df.describe()

# %% [markdown]
# ## 3. Análise da Variável Alvo (Class)

# %%
print(df['Class'].value_counts())
print("\n--- Proporção de Classes (%) ---")
print(df['Class'].value_counts(normalize=True) * 100)

sns.countplot(x='Class', data=df)
plt.title('Distribuição das Classes (0: Não Fraude, 1: Fraude)')
plt.show()

sns.countplot(data=df, x='Amount', hue='Class')
plt.title('Distribuição do Valor da Transação por Classe')
plt.show()
# %% [markdown]
# ## 4. Análise de 'Time' e 'Amount'

# %%
sns.histplot(df['Time'], bins=50, kde=True)
plt.title('Distribuição do Tempo de Transação')
plt.show()

# %%
sns.histplot(df['Amount'], bins=100, kde=True)
plt.title('Distribuição do Valor da Transação')
plt.xlim(0, 5000)
plt.show()

# %% [markdown]
# ## 5. Matriz de Correlação

# %%
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
# %%
