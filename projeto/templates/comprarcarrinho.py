import streamlit as st
import pandas as pd
import time
from datetime import datetime
from views import View
from models.venda import Venda, VendaDAO

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
            st.warning("Carrinho vazio! Não é possível finalizar a compra.")
            return

    
        for item in carrinho:
            produto = item["produto"]
            qtd = item["qtd"]
            novo_estoque = produto.get_estoque() - qtd
            View.produto_atualizar(
                produto.get_id(),
                produto.get_descricao(),
                produto.get_preco(),
                novo_estoque,
                produto.get_id_categoria()
            )


        lista_itens = [{"produto": item["produto"].get_descricao(), "qtd": item["qtd"]} for item in carrinho]
        lista_carrinho = [item["produto"].get_id() for item in carrinho]  # apenas os IDs do produto

      
        id_cliente = st.session_state.get("cliente_id", 0)  # se não tiver, coloca 0

     
        venda = Venda(
            id=0,
            data=datetime.now().strftime("%d/%m/%Y %H:%M"),
            carrinho=lista_carrinho,
            itens=lista_itens,
            total=total,
            id_venda=0,
            id_cliente=id_cliente
        )


        VendaDAO.inserir(venda)

    
        st.session_state.carrinho = []

        st.success("Compra realizada com sucesso!")
        time.sleep(1)