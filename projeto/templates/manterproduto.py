import streamlit as st
import pandas as pd
import time
from views import View
from models.produto import Produto, ProdutoDAO

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produto = View.produto_listar()
  
        if len(produto) == 0: st.write("Nenhum produto cadastrado")
        else:
            list_dic = []
            for obj in produto: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["descricao", "preco", "estoque", "id_categoria"])

    def inserir():
        descricao = st.text_input("Informe a descrição")
        preco = st.text_input("Informe o preço")
        estoque = st.text_input("Informe a quantidade")
        id_categoria = st.text_input("Informe o id da categoria")
        if st.button("Inserir"):
            try:
                View.produto_inserir(descricao, preco, estoque, id_categoria)
                st.success("Produto inserida com sucesso")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produto)
            id = st.text_input("Informe o novo id", op.get_id())
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            preco = st.text_input("Informe o novo preço", op.get_preco())
            estoque = st.text_input("Informe a nova quantidade", op.get_estoque())
            id_categoria = st.text_input("Informe o novo id da categoria", op.get_id_categoria())
            if st.button("Atualizar"):
                id = op.get_id()
                View.produto_atualizar(id, descricao, preco, estoque, id_categoria)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produto = View.produto_listar()
        if len(produto) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produto)
            if st.button("Excluir"):
                id = op.get_id()
                View.produto_excluir(id)
                st.success("Produto excluída com sucesso")
                time.sleep(2)
                st.rerun()