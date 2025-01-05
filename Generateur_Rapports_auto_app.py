import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Générateur de Rapports Automatisés')

# URL du fichier CSV d'exemple
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# Lecture du fichier CSV directement depuis l'URL
df = pd.read_csv(csv_url)

st.write("Aperçu des données:")
st.write(df.head())

# Sélection des colonnes pour l'analyse
columns = df.columns.tolist()
selected_columns = st.multiselect("Sélectionnez les colonnes à analyser", columns)

if selected_columns:
 st.write("Statistiques descriptives:")
 st.write(df[selected_columns].describe())

# Visualisation des données
st.write("Visualisations:")

for column in selected_columns:
    st.write(f"Distribution de {column}:")
    plt.figure(figsize=(10, 4))
    sns.histplot(df[column], kde=True)
    st.pyplot(plt)
    st.write(f"Boîte à moustaches de {column}:")
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=df[column])
    st.pyplot(plt)