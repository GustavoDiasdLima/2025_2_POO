import streamlit as st
import pandas as pd

class VisualizarCarrinhoUI:

    @staticmethod
    def iniciar_sessao():
        if "carrinho" not in st.session_state:
            st.session_state.carrinho = []

    @staticmethod
    def main():
        VisualizarCarrinhoUI.iniciar_sessao()

        st.header("Carrinho")

        carrinho = st.session_state.carrinho
        if not carrinho:
            st.info("Seu carrinho está vazio.")
            return

        dados = []
        total = 0
        for item in carrinho:
            produto = item["produto"]
            qtd = item["qtd"] 
            subtotal = produto.get_preco() * qtd
            total += subtotal

            dados.append({
                "Produto": produto.get_descricao(),
                "Quantidade": qtd,
                "Preço Unitário": produto.get_preco(),
                "Subtotal": subtotal
            })

        df = pd.DataFrame(dados)
        st.table(df)
        st.write(f"### Total: R$ {total:.2f}")
