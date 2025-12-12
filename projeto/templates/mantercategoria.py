import streamlit as st
import pandas as pd
import time
from views import View
from models.categoria import Categoria, CategoriaDAO


class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    def listar():
        categoria = View.categoria_listar()
       
        if len(categoria) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            list_dic = []
            for obj in categoria: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True, column_order=["id", "descricao"])

    def inserir():
        descricao = st.text_input("Informe a categoria")
        if st.button("Inserir"):
            try:
                View.categoria_inserir(descricao)
                st.success("Categoria inserida com sucesso")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        categoria = View.categoria_listar()
        if len(categoria) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Categorias", categoria)
            descricao = st.text_input("Informe a nova categoria", op.get_descricao())
            if st.button("Atualizar"):
                id = op.get_id()
                View.categoria_atualizar(id, categoria)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        categoria = View.categoria_listar()
        if len(categoria) == 0: st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categoria)
            if st.button("Excluir"):
                id = op.get_id()
                View.categoria_excluir(id)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
        