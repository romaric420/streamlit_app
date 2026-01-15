# pages/5_visualisation.py
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Visualisation', layout='wide')

st.title('Visualisation des données')

# Vérifier si le DataFrame est disponible dans la session
if 'df' in st.session_state:
    df = st.session_state['df']

    # Sélection des colonnes pour l'axe X et Y
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns

    if len(numeric_columns) >= 2:
        x_axis = st.selectbox('Sélectionnez la colonne pour l\'axe X', options=numeric_columns)
        y_axis = st.selectbox('Sélectionnez la colonne pour l\'axe Y', options=numeric_columns)

        # Créer le graphique Plotly
        fig = px.scatter(df, x=x_axis, y=y_axis)

        # Afficher le graphique
        st.plotly_chart(fig)
    else:
        st.warning('Le fichier CSV doit contenir au moins deux colonnes numériques.')
else:
    st.error('Aucun DataFrame trouvé. Veuillez charger un fichier CSV depuis la page d\'accueil.')
