import streamlit as st
import pandas as pd
import time
from datetime import date
from models.entrega import Entrega, EntregaDAO
from models.venda import Venda, VendaDAO
from models.promocao import PromocaoDAO
from models.vendaitem import VendaItem, VendaItemDAO


class ComprarCarrinhoUI:

    @staticmethod
    def iniciar_sessao():
        if "carrinho" not in st.session_state:
            st.session_state.carrinho = []

    @staticmethod
    def main():
        ComprarCarrinhoUI.iniciar_sessao()
        st.header("Carrinho")

        carrinho = st.session_state.carrinho

        if not carrinho:
            st.info("Seu carrinho está vazio.")
            return

        dados = []
        total = 0

        for item in carrinho:
            produto = item["produto"]
            qtd = item["qtd"]
            subtotal = produto.get_preco() * qtd
            total += subtotal

            dados.append({
                "Produto": produto.get_descricao(),
                "Quantidade": qtd,
                "Preço Unitário": produto.get_preco(),
                "Subtotal": subtotal
            })

        st.table(pd.DataFrame(dados))
        st.write(f"### Total da compra: R$ {total:.2f}")

        if st.button("Finalizar Compra"):
            ComprarCarrinhoUI.finalizar_compra(total)


    @staticmethod
    def finalizar_compra(total):
        carrinho = st.session_state.carrinho

        if not carrinho:
            st.warning("Carrinho vazio!")
            return

        id_cliente = st.session_state.get("cliente_id", 0)
        id_venda = VendaDAO.proximo_id()
        data = date.today().strftime("%d/%m/%Y")

  
        venda = Venda(
            id_venda,
            data,
            total,
            id_cliente
        )
        VendaDAO.inserir(venda)

  
        for item in carrinho:
            produto = item["produto"]
            qtd = item["qtd"]

            vi = VendaItem(
                VendaItemDAO.proximo_id(),
                qtd,
                produto.get_preco(),
                id_venda,
                produto.get_id()
            )
            VendaItemDAO.inserir(vi)

   
        endereco = st.text_input("Digite o seu endereço para entrega:")

        if not endereco:
            st.warning("Insira o endereço para concluir a compra.")
            return

    
        from datetime import datetime, timedelta
        previsao = (datetime.now() + timedelta(minutes=30)).strftime("%d/%m/%Y %H:%M")

    
        entrega = Entrega(
            EntregaDAO.proximo_id(),
            id_venda,
            endereco,     
            "Preparando",
            previsao    
        )
        EntregaDAO.inserir(entrega)

   
        st.session_state.carrinho = []

        st.success("Compra realizada com sucesso! 🛒")
        st.info(f"Endereço: {endereco}\nPrevisão de entrega: {previsao}")
        time.sleep(1)
        st.rerun()
