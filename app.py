from plot.interactive import plot_line_i as pli
import streamlit as st

st.title('Preços de Ações App')

# Sidebar
st.sidebar.header('Consulta')
symbol = st.sidebar.text_input('Digite um ativo:', 'AAPL')
st.pyplot_chart(pli(symbol))
