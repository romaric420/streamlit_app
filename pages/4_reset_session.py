# pages/4_reset_session.py
import streamlit as st

st.set_page_config(page_title='Reset', layout='wide')

st.title('Réinitialiser l\'état de la session')

if st.button('Réinitialiser le compteur'):
    st.session_state.compteur = 0
    st.success('Le compteur a été réinitialisé.')

if st.button('Réinitialiser la sélection'):
    st.session_state.selection = []
    st.success('La sélection a été réinitialisée.')
