import streamlit as st
import pandas as pd

class ListarMinhasComprasUI:

    @staticmethod
    def main():
        st.header("Minhas Compras")

        compras = st.session_state.get("compras", [])

        if not compras:
            st.info("Nenhuma compra realizada até agora.")
            return

        for idx, compra in enumerate(compras):
            st.write(f"### Compra #{idx+1} — Total: R$ {compra['total']:.2f}")
            df = pd.DataFrame(compra["itens"])
            st.table(df)
            st.divider()