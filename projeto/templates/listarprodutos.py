import streamlit as st
import pandas as pd
from views import View

class ListarProdutosUI:
    @staticmethod
    def main():
        st.header("Produtos Disponíveis")
        produtos = View.produto_listar()
        if not produtos:
            st.info("Nenhum produto cadastrado.")
            return

        dados = [p.to_json() for p in produtos]
        df = pd.DataFrame(dados)
        st.dataframe(df, hide_index=True,
                     column_order=["descricao", "preco", "estoque", "id_categoria"])