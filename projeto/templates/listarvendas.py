
import streamlit as st
import pandas as pd
import time
from views import View

class ListarVendasUI:
    @staticmethod
    def main():
        st.header("Listar Vendas")
        tabs = st.tabs(["Visualizar"])

        with tabs[0]:
            ListarVendasUI.listar()

    @staticmethod
    def listar():

        if "cliente_id" not in st.session_state:
            st.error("Nenhuma venda realizada.")
            return
        
        id_cliente = st.session_state["cliente_id"]
        itens = View.carrinho_listar(id_cliente)

        if len(itens) == 0:
            st.write("Carrinho vazio")
            return

        lista_dic = []
        for item in itens:
            lista_dic.append({
                "Produto": item.get_produto().get_descricao(),
                "Quantidade": item.get_qtd(),
                "Preço Unitário": item.get_produto().get_preco(),
                "Subtotal": item.get_subtotal()
            })

        df = pd.DataFrame(lista_dic)
        st.dataframe(df, hide_index=True)

        st.subheader(f"Total do Carrinho: R$ {sum(i.get_subtotal() for i in itens):.2f}")


        nomes_itens = [
            f"{item.get_produto().get_descricao()} - {item.get_quantidade()}un"
            for item in itens
        ]

        escolha = st.selectbox("Selecione um item para remover", nomes_itens)

        if st.button("Remover Item"):
            try:
                index = nomes_itens.index(escolha)
                item_escolhido = itens[index]

                View.carrinho_remover(id_cliente, item_escolhido.get_produto().get_id())

                st.success("Item removido com sucesso!")
            except Exception as erro:
                st.error(erro)

            time.sleep(2)
            st.rerun()
