
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('RECLAMEAQUI_HAPVIDA.csv')

# Gráfico de linhas para o número único de IDs ao longo do tempo
status = st.selectbox(
    'status:',
    df["STATUS"].unique()
)
filtered_df = df[df["STATUS"] == status]
filtered_df['TEMPO'] = pd.to_datetime(filtered_df['TEMPO'])
fig, ax = plt.subplots()
filtered_df.groupby('TEMPO').nunique()['ID'].plot(ax=ax, marker='o', linestyle='-', color='b', label='Número único de IDs')
ax.set_title('Número de reclamações por mês em 2022')
ax.set_xlabel('Mês')
ax.set_ylabel('Número de reclamações')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Gráfico de barras para a frequência de reclamações por estado
estado_lista = [estado.split('-', 2)[1].strip() for estado in filtered_df['LOCAL']]
filtered_df['ESTADO'] = estado_lista
dados_agrupados_estado = filtered_df.groupby('ESTADO')['ID'].sum().reset_index()

fig_estado = plt.figure(figsize=(10, 6))
plt.bar(dados_agrupados_estado['ESTADO'], dados_agrupados_estado['ID'], color='skyblue')
plt.xlabel('Estado')
plt.ylabel('Reclamações')
plt.title('Frequência de reclamações por estado')
st.pyplot(fig_estado)

# Gráfico de barras para a frequência de reclamações por status
dados_agrupados_status = filtered_df.groupby('STATUS')['ID'].sum().reset_index()

fig_status = plt.figure(figsize=(10, 6))
plt.bar(dados_agrupados_status['STATUS'], dados_agrupados_status['ID'], color='skyblue')
plt.xlabel('Status')
plt.ylabel('Frequência')
plt.title('Frequência de reclamações por status')
st.pyplot(fig_status)

# Histograma para a distribuição do tamanho do texto na coluna DESCRICAO
filtered_df['TAMANHO_DESCRICAO'] = filtered_df['DESCRICAO'].apply(len)
fig_hist = plt.figure()
plt.hist(filtered_df['TAMANHO_DESCRICAO'], edgecolor='black')
plt.title('Distribuição do tamanho do texto: DESCRICAO')
plt.xlabel('Tamanho do texto')
plt.ylabel('Frequência')
st.pyplot(fig_hist)
