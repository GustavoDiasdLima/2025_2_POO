import math
import pandas as pd
import streamlit as st

class Equacao: 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0: raise ValueError("Não é uma equação do segundo grau")
    def delta(self):
        return self.b**2 - 4 * self.a * self.c
    def x1(self):
        delta = self.delta()
        if delta >= 0: return (-self.b + math.sqrt(delta)) / (2 * self.a)
        return f"{-self.b / (2 * self.a)} + {math.sqrt(-delta) / (2 * self.a)}i"
    def x2(self):
        delta = self.delta()
        if delta >= 0: return (-self.b + math.sqrt(delta)) / (2 * self.a)
    def __str__(self):
        return f"{self.a}x^2, {self.b}x, {self.c}"
        return f"{self.a}, {self.b}, {self.c}"
    def ponto_inflexao(self):
        return -self.b / (2 * self.a)
    def y(self, x):
        return self.a * x * x + self.b * x + self.c


f = Equacao(1, -5, 6)
print(f)
print(f.delta(), f.x1(), f.x2())
print(f.ponto_inflexao())

p = f.ponto_inflexao()
xmin = p - 10
xmax = p + 10
npontos = 11
dist = (xmax - xmin ) / npontos
px = []
py = []
x = min

while x < xmax:
    px.append(x)
    p.append(y)
    y = f.y
    print(x, y)
    x += dist

    df = pd.DataFrame(
        {  
            "x": px,
            "y": py,
        }
    )
    st.line_chart(df, x="x", y="y")
    

