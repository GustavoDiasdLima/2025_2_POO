import streamlit as st
from templates.mantercategoria import ManterCategoriaUI
from templates.mantercliente import ManterClienteUI
from templates.manterproduto import ManterProdutoUI
from templates.reajustarproduto import ReajustarProdutoUI
from templates.visualizarcarrinho import VisualizarCarrinhoUI
from templates.listarvendas import ListarVendasUI
from templates.listarprodutos import ListarProdutosUI
from templates.listarminhascompras import ListarMinhasComprasUI
from templates.inserirprodcarrinho import InserirProdutoCarrinhoUI
from templates.comprarcarrinho import ComprarCarrinhoUI
from templates.login import LoginUI
from templates.abrir import AbrirUI
from templates.feedback import FeedbackUI
from templates.entrega import EntregaUI
from templates.promocoes_admin import PromocaoUI
from templates.wishlist import WishlistUI

from views import View

class IndexUI:
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Categorias",
            "Cadastro de Clientes",
            "Cadastro de Produtos",
            "Reajustar Produtos",  
            "Listar Vendas",
            "Promoção"
            ])
        #st.session_state["opcao"].append(op)
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()
        if op == "Listar Vendas": ListarVendasUI.main()
        if op == "Promoção": PromocaoUI.main()

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no Sistema", 
            "Abrir Conta"])
                   
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirUI.main()
        return
    
    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar Produtos",
            "Inserir Produto no Carrinho",
            "Visualizar Carrinho",
            "Comprar o Carrinho",
            "Listar Minhas Compras", "Minhas Entregas", "Feedback", "Wishlist"])
                   
        if op == "Listar Produtos": ListarProdutosUI.main()
        if op == "Inserir Produto no Carrinho": InserirProdutoCarrinhoUI.main()
        if op == "Visualizar Carrinho": VisualizarCarrinhoUI.main()
        if op == "Comprar o Carrinho": ComprarCarrinhoUI.main()
        if op == "Listar Minhas Compras": ListarMinhasComprasUI.main()
        if op == "Minhas Entregas": EntregaUI.main()
        if op == "Feedback": FeedbackUI.main()
        if op == "Wishlist": WishlistUI.main()
        return op

    @staticmethod
    def sidebar():
        if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
            # usuário está logado, verifica se é o admin
            admin = st.session_state["cliente_nome"] == "admin"
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema() 
    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()
    @staticmethod
    def main():
        #if "opcao" not in st.session_state: st.session_state["op"] = []
        #st.write(st.session_state)
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()