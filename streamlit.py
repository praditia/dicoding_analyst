import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set(style="dark")


def create_season_df(df):
    return df.groupby("season")["total_count"].sum().reset_index()


def create_workingday_df(df):
    return df.groupby("workingday")["total_count"].sum().reset_index()


hour_df = pd.read_csv("hour_data.csv")

season_df = create_season_df(hour_df)
workingday_df = create_workingday_df(hour_df)

st.header("Bike Sharing Dashboard :bike:")

st.subheader("Number of Bike Rentals by Season")
fig, ax = plt.subplots(figsize=(10, 5))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    y="total_count",
    x="season",
    data=season_df.sort_values(by="total_count", ascending=False),
    palette=colors,
    ax=ax,
)
plt.ylabel(None)
st.pyplot(fig)


st.subheader("Number of Bikes Rental by Working Day")

labels = workingday_df["workingday"]
sizes = workingday_df["total_count"]

colors = ("#D3D3D3", "#72BCD4")

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, wedgeprops={"width": 0.4}, startangle=0)

plt.title("Total Bikes Rental by Working Day")
plt.axis("equal")
st.pyplot(fig)

st.subheader("Monthly distribution of bike rental counts")
fig, ax = plt.subplots()
sns.barplot(data=hour_df[["month", "total_count"]], x="month", y="total_count", ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Bike rental counts")
plt.xlabel("Month")
st.pyplot(fig)

st.subheader("Correlation of Bike Sharing Counts")
corrMatt = hour_df[["temperature", "humidity", "windspeed", "total_count"]].corr()

mask = np.array(corrMatt)

mask[np.tril_indices_from(mask)] = False
fig, ax = plt.subplots()
sns.heatmap(corrMatt, mask=mask, vmax=0.8, square=True, annot=True, ax=ax)
st.pyplot(fig)
