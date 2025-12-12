
import pandas as pd 
from views import View
import streamlit as st

class AbrirUI:
    def main():
        st.header("Abrir Conta")
        nome = st.text_input("Informe seu nome")
        email = st.text_input("Informe seu email")
        fone = st.text_input("Informe seu telefone")
        senha = st.text_input("Informe sua senha", type="password")
        if st.button("Criar Conta"):
            c = View.cliente_inserir(nome, email, fone, senha)
            st.rerun()