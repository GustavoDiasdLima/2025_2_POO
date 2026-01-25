import streamlit as st
from datetime import datetime
from models.promocao import Promocao, PromocaoDAO

class PromocaoUI:

    @staticmethod
    def main():
        st.header("Gerenciar Promoções")

        st.subheader("Cadastrar nova promoção")
        titulo = st.text_input("Título")
        descricao = st.text_area("Descrição")
        desconto = st.number_input("Desconto (%)", min_value=1, max_value=100, step=1)
        data_inicio = st.date_input("Data de início")
        data_fim = st.date_input("Data de fim")

        if st.button("Cadastrar Promoção"):
            if not titulo.strip() or not descricao.strip():
                st.warning("Preencha título e descrição.")
            elif data_fim < data_inicio:
                st.warning("Data de fim não pode ser anterior à data de início.")
            else:
                id_promocao = PromocaoDAO.proximo_id()
                p = Promocao(
                    id_promocao,
                    titulo,
                    descricao,
                    desconto,
                    data_inicio.strftime("%Y-%m-%d"),
                    data_fim.strftime("%Y-%m-%d")
                )
                PromocaoDAO.inserir(p)
                st.success(f"Promoção '{titulo}' cadastrada com sucesso!")

        st.divider()
        st.subheader("Promoções Ativas")
        ativas = PromocaoDAO.listar_ativas()
        if ativas:
            for p in ativas:
                st.info(
                    f"{p.get_titulo()} — {p.get_descricao()} — "
                    f"Desconto: {p.get_desconto()}% — "
                    f"Validade: {p.get_data_inicio()} até {p.get_data_fim()}"
                )
        else:
            st.info("Nenhuma promoção ativa no momento.")
