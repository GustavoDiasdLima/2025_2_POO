import streamlit as st
import from retangulo import Retangulo
import pandas

st.header("Calculo com Retângulo")
b = st.text_input("Informe a base")
h = st.text_input("Informe a altura")
if st.button("Calcular"):
    r = Retangulo(float(b), float(h))
    st.write(f"Área = {r.calc_area()}")
    st.write(f"Diagonal = {r.calc_diagonal()}")
    st.write(r)
    

    df = pd.DataFrame(
    {
        "x": [1, 2, 3],
        "y": [4, 5, 6]
    }
)
st.line_chart(df, x="x", y="y")