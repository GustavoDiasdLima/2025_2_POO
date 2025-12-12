import streamlit as st
import time
from views import View

class InserirProdutoCarrinhoUI:

    @staticmethod
    def iniciar_sessao():
        if "carrinho" not in st.session_state:
            st.session_state.carrinho = []

    @staticmethod
    def main():
        InserirProdutoCarrinhoUI.iniciar_sessao()

        st.header("Adicionar Produto ao Carrinho")

        produtos = View.produto_listar()
        if not produtos:
            st.warning("Nenhum produto disponível.")
            return

        produto = st.selectbox("Selecione o produto", produtos, format_func=lambda p: f"{p.get_descricao()} - R$ {p.get_preco():.2f}")
        qtd = st.number_input("Quantidade", min_value=1, step=1)

        if st.button("Adicionar ao Carrinho"):
            if qtd > produto.get_estoque():
                st.error("Quantidade maior que o estoque disponível.")
                return

    
            st.session_state.carrinho.append({
                "produto": produto,
                "qtd": qtd
            })

            st.success(f"{produto.get_descricao()} adicionado ao carrinho!")
            time.sleep(1)
         