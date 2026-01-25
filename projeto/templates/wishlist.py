
import streamlit as st
import pandas as pd
from models.wishlist import Wishlist, WishlistDAO
from models.produto import ProdutoDAO

class WishlistUI:

    @staticmethod
    def main():
        st.header("Minha Wishlist")

        id_cliente = st.session_state.get("cliente_id", 0)
        if id_cliente == 0:
            st.warning("Cliente não identificado.")
            return

     
        def carregar_wishlist():
            produtos_wishlist = WishlistDAO.listar_por_cliente(id_cliente)
            dados = []
            for w in produtos_wishlist:
                produto = ProdutoDAO.listar_id(w.get_id_produto())
                if produto:
                    dados.append({
                        "id_wishlist": w.get_id(),   
                        "Produto": produto.get_descricao(),
                        "Preço": round(produto.get_preco(), 2)
                    })
            return dados

        dados = carregar_wishlist()

        if not dados:
            st.info("Sua wishlist está vazia.")
        else:
            df = pd.DataFrame(dados).drop(columns="id_wishlist")  
            st.table(df)

            
            for linha in dados:
                produto = linha["Produto"]
                id_w = linha["id_wishlist"]
                if st.button(f"Remover {produto}", key=f"rm_{id_w}"):
                    WishlistDAO.remover(id_cliente, ProdutoDAO.listar_descricao(produto).get_id())
                    st.success(f"{produto} removido da wishlist!")
                    dados = carregar_wishlist()  
                    break  

       
        todos_produtos = ProdutoDAO.objetos
        produto_selecionado = st.selectbox(
            "Adicionar produto à wishlist",
            todos_produtos,
            format_func=lambda p: p.get_descricao()
        )

        if st.button("Adicionar à Wishlist"):
           
            existente = any(
                w.get_id_produto() == produto_selecionado.get_id() and w.get_id_cliente() == id_cliente
                for w in WishlistDAO.objetos
            )
            if existente:
                st.warning("Produto já está na wishlist!")
            else:
                id_w = WishlistDAO.proximo_id()
                w = Wishlist(id_w, id_cliente, produto_selecionado.get_id())
                WishlistDAO.inserir(w)
                st.success(f"{produto_selecionado.get_descricao()} adicionado à wishlist!")
                dados = carregar_wishlist()  

