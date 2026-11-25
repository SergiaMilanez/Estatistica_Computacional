from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Estatística Computacional — Grupo 03', layout='wide', initial_sidebar_state='collapsed')
root = Path(__file__).resolve().parent
page = root / 'Estatistica_Computacional_v16.html'
if page.is_file():
    content = page.read_text(encoding='utf-8')
    st.download_button('Baixar página completa para consulta offline', data=content.encode('utf-8'), file_name=page.name, mime='text/html')
    components.html(content, height=1000, scrolling=True)
else:
    st.error('Arquivo Estatistica_Computacional_v16.html não encontrado no repositório.')
