from templates.mantercategoria import ManterCategoriaUI
from templates.mantercliente import ManterClienteUI
from templates.manterproduto import ManterProdutoUI
from templates.reajustarproduto import ReajustarProdutoUI
from templates.login import LoginUI
import streamlit as st

class IndexUI:

    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Categorias",
            "Cadastro de Clientes",
            "Cadastro de Produtos",
            "Reajustar Produtos"])
        #st.session_state["opcao"].append(op)
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de serviços": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()

    def menu_visitante():
        op = st.sidebrar.selectbox("Menu", [
            "Entrar no Sistema", 
            "Abrir Conta"])
                   
        if op == "Entrar no Sistema": LoginUI.main()
        if op == 2: IndexUI.visitante_criar_conta()
        return op

    def sidebar():
        if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
        else: IndexUI.menu_admin()
        IndexUI.menu_admin()

    def main():
        if "opcao" not in st.session_state: st.session_state["op"] = []
        st.write(st.session_state)
        IndexUI.sidebar()

IndexUI.main()