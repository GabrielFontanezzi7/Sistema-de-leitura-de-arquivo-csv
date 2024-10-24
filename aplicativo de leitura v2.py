import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados (altere o caminho do arquivo para o seu arquivo de dados)
df = pd.read_excel('Sistematização.xlsx', 'Página1')

# Remover duplicatas
df_sem_duplicatas = df.drop_duplicates()

# Função para calcular as estatísticas solicitadas
def calcular_estatisticas(df):
    estatisticas = {
        'Idade': {
            'Média': df['Idade'].mean(),
            'Moda': df['Idade'].mode()[0],
            'Mediana': df['Idade'].median(),
            'Valor Máximo': df['Idade'].max(),
            'Valor Mínimo': df['Idade'].min(),
            'Desvio Padrão': df['Idade'].std()
        },
        'Renda Anual': {
            'Média': df['Renda anual'].mean(),
            'Moda': df['Renda anual'].mode()[0],
            'Mediana': df['Renda anual'].median(),
            'Valor Máximo': df['Renda anual'].max(),
            'Valor Mínimo': df['Renda anual'].min(),
            'Desvio Padrão': df['Renda anual'].std()
        },
        'Número de filhos': {
            'Média': df['Número de filhos'].mean(),
            'Moda': df['Número de filhos'].mode()[0],
            'Mediana': df['Número de filhos'].median(),
            'Valor Máximo': df['Número de filhos'].max(),
            'Valor Mínimo': df['Número de filhos'].min(),
            'Desvio Padrão': df['Número de filhos'].std()
        },
        'Horas de trabalho por semana': {
            'Média': df['Horas de trabalho por semana'].mean(),
            'Moda': df['Horas de trabalho por semana'].mode()[0],
            'Mediana': df['Horas de trabalho por semana'].median(),
            'Valor Máximo': df['Horas de trabalho por semana'].max(),
            'Valor Mínimo': df['Horas de trabalho por semana'].min(),
            'Desvio Padrão': df['Horas de trabalho por semana'].std()
        },
        'Nível de satisfação com o trabalho atual': {
            'Média': df['Nível de satisfação com o trabalho atual'].mean(),
            'Moda': df['Nível de satisfação com o trabalho atual'].mode()[0],
            'Mediana': df['Nível de satisfação com o trabalho atual'].median(),
            'Valor Máximo': df['Nível de satisfação com o trabalho atual'].max(),
            'Valor Mínimo': df['Nível de satisfação com o trabalho atual'].min(),
            'Desvio Padrão': df['Nível de satisfação com o trabalho atual'].std()
        }
    }
    return estatisticas

# Calcular estatísticas após remoção das duplicatas
estatisticas = calcular_estatisticas(df_sem_duplicatas)

# Exibir as estatísticas
for coluna, stats in estatisticas.items():
    print(f"\nEstatísticas para {coluna}:")
    for key, value in stats.items():
        print(f"{key}: {value}")

# Gráfico de dispersão entre Idade e Renda Anual
plt.figure(figsize=(10, 6))
plt.scatter(df_sem_duplicatas['Idade'], df_sem_duplicatas['Renda anual'], alpha=0.5)
plt.title('Relação entre Idade e Renda Anual')
plt.xlabel('Idade')
plt.ylabel('Renda Anual')
plt.grid(True)
plt.show()

# Calcular correlação entre Idade e Renda Anual
correlacao = df_sem_duplicatas[['Idade', 'Renda anual']].corr().iloc[0, 1]
print(f"\nCorrelação entre Idade e Renda Anual: {correlacao:.2f}")

# Gráfico de dispersão entre Nível de Satisfação e Renda Anual
plt.figure(figsize=(10, 6))
plt.scatter(df_sem_duplicatas['Nível de satisfação com o trabalho atual'], df_sem_duplicatas['Renda anual'], alpha=0.5)
plt.title('Relação entre Nível de Satisfação e Renda Anual')
plt.xlabel('Nível de Satisfação com o Trabalho Atual')
plt.ylabel('Renda Anual')
plt.grid(True)
plt.show()

# Calcular correlação entre Nível de Satisfação e Renda Anual
correlacao_satisfacao_renda = df_sem_duplicatas[['Nível de satisfação com o trabalho atual', 'Renda anual']].corr().iloc[0, 1]
print(f"\nCorrelação entre Nível de Satisfação e Renda Anual: {correlacao_satisfacao_renda:.2f}")
