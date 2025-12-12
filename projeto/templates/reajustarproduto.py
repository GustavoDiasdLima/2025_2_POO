import streamlit as st
import pandas as pd
import time
from views import View
from models.cliente import Cliente, ClienteDAO
from models.produto import Produto, ProdutoDAO
from models.categoria import Categoria, CategoriaDAO

class ReajustarProdutoUI:
    def main():
        st.header("Reajustar Produtos")

    
        tab1, tab2 = st.tabs(["Listar", "Reajustar Preço"])

        with tab1:
            ReajustarProdutoUI.listar()

        with tab2:
            ReajustarProdutoUI.reajustar()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produtos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True,
                         column_order=["descricao", "preco", "estoque", "id_categoria"])

    def reajustar():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto para reajustar o preço", produtos)

            preco_atual = float(op.get_preco())
            st.write(f"**Preço atual:** R$ {preco_atual:.2f}")

            percentual = st.number_input("Informe o percentual de reajuste (%)", step=0.1)

            if st.button("Reajustar Preço"):
                try:
                    novo_preco = preco_atual * (1 + percentual/100)

                    
                    View.produto_atualizar(
                        op.get_id(),
                        op.get_descricao(),
                        novo_preco,
                        op.get_estoque(),
                        op.get_id_categoria()
                    )

                    st.success(f"Preço reajustado para R$ {novo_preco:.2f}")
                except Exception as erro:
                    st.error(erro)

                time.sleep(2)
                st.rerun()