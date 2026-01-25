import streamlit as st
from views import View

class EntregaUI:

    @staticmethod
    def main():
        st.header("Minhas Entregas")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.warning("Cliente não identificado.")
            return

        vendas = View.venda_listar(id_cliente)

        if not vendas:
            st.info("Você ainda não realizou nenhuma compra.")
            return

        for venda in vendas:
            st.subheader(f"Compra #{venda.get_id()} — Total R$ {venda.get_total():.2f}")

            entrega = View.entrega_buscar_por_venda(venda.get_id())

            if entrega:
                st.write(f" **Endereço:** {entrega.get_endereco()}")
                st.write(f" **Status:** {entrega.get_status()}")
                st.write(f" **Previsão:** {entrega.get_previsao()}")
            else:
                st.warning("Entrega ainda não cadastrada.")

            st.divider()
