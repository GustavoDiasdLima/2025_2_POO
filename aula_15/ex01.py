import streamlit as st
import pandas

st.header("Olá mundo!")
st.write("Teste") #o print é o .write
if st.button("Clique aqui"):
    st.write("Bem-vindo")


df = pd.DataFrame(
    {
        "x": [1, 2, 3],
        "y": [4, 5, 6]
    }
)
st.line_chart(df, x="x", y="y")