import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({"c1": [1, 2, 3, 4], "c2": [10, 20, 30, 40]})

st.dataframe(data=df, width=500, height=150)

st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.json(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
