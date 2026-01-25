import streamlit as st
from views import View
from models.feedback import Feedback, FeedbackDAO
from datetime import date

class FeedbackUI:

    @staticmethod
    def main():
        st.header("Avaliar Produto")

        id_cliente = st.session_state.get("cliente_id")
        if id_cliente is None:
            st.warning("Cliente não identificado.")
            return

      
        produtos = View.produto_listar()
        if not produtos:
            st.info("Nenhum produto disponível para avaliação.")
            return

        produto = st.selectbox(
            "Selecione o produto",
            produtos,
            format_func=lambda p: p.get_descricao()
        )

        nota = st.slider("Nota", 1, 5)
        comentario = st.text_area("Comentário")

        if st.button("Enviar Feedback"):
            if not comentario.strip():
                st.warning("Escreva um comentário antes de enviar.")
                return

   
            data = date.today().strftime("%d/%m/%Y")


            id_feedback = FeedbackDAO.proximo_id()

        
            feedback = Feedback(
                id_feedback,
                nota,          
                comentario,    
                data,
                id_cliente
            )

          
            FeedbackDAO.inserir(feedback)

            st.success("Feedback enviado com sucesso! ✅")
