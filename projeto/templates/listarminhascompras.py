import streamlit as st
import pandas as pd
from views import View
from models.entrega import EntregaDAO  # Importar o DAO da entrega

class ListarMinhasComprasUI:

    @staticmethod
    def main():
        st.header("Minhas Compras")

        id_cliente = st.session_state["cliente_id"]
        vendas = View.venda_listar(id_cliente)

        if not vendas:
            st.info("Nenhuma compra realizada até agora.")
            return

        for venda in vendas:
            st.subheader(
                f"Venda #{venda.get_id()} — Total: R$ {venda.get_total():.2f}"
            )

            # Listar itens da venda
            itens = View.vendaitem_listar_por_venda(venda.get_id())
            dados = []
            for item in itens:
                dados.append({
                    "Produto ID": item.get_id_produto(),
                    "Quantidade": item.get_qtd(),
                    "Preço": item.get_preco(),
                    "Subtotal": item.get_qtd() * item.get_preco()
                })
            st.table(pd.DataFrame(dados))

            # 🔹 Aqui: listar entrega da venda
            entrega = EntregaDAO.listar_por_venda(venda.get_id())
            if entrega:
                st.info(f"Entrega: {entrega.get_endereco()} — Previsão: {entrega.get_previsao()} — Status: {entrega.get_status()}")
            else:
                st.warning("Entrega ainda não cadastrada.")

            st.divider()
