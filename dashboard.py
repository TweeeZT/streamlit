import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

@st.cache_data
def load_data():
    df = pd.read_csv("merged_data.csv")  
    
    day_mapping = {0: "Senin", 1: "Selasa", 2: "Rabu", 3: "Kamis", 4: "Jumat", 5: "Sabtu", 6: "Minggu"}
    workday_mapping = {0: "Weekend", 1: "Workday"}
    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    year_mapping = {0: "2011", 1: "2012"}
    
    df["weekday_hari"] = df["weekday_hari"].map(day_mapping)
    df["workingday_hari"] = df["workingday_hari"].map(workday_mapping)
    df["season_hari"] = df["season_hari"].map(season_mapping)
    df["yr_hari"] = df["yr_hari"].map(year_mapping)
    
    return df

df = load_data()

st.title("Dashboard Analisis Data Rental Sepeda")
st.sidebar.header("Filter Data")

years = df["yr_hari"].unique()
seasons = df["season_hari"].unique()
selected_year = st.sidebar.selectbox("Pilih Tahun", years)
selected_season = st.sidebar.selectbox("Pilih Musim", seasons)

df_filtered = df[(df["yr_hari"] == selected_year) & (df["season_hari"] == selected_season)]

day_usage = df.groupby("weekday_hari")["cnt_hari"].sum().reset_index()
st.subheader("Total Rental Berdasarkan Hari")
plt.figure(figsize=(8, 4))
sns.barplot(x=day_usage["weekday_hari"], y=day_usage["cnt_hari"], palette="pastel")
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Perbandingan Rental antara Workday dan Weekend")
workday_vs_weekend = df.groupby("workingday_hari")["cnt_hari"].sum().reset_index()
plt.figure(figsize=(6, 4))
sns.barplot(x=workday_vs_weekend["workingday_hari"], y=workday_vs_weekend["cnt_hari"], palette="coolwarm")
plt.xlabel("Kategori Hari")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Total Penyewaan Berdasarkan Musim")
season_usage = df.groupby("season_hari")["cnt_hari"].sum().reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x=season_usage["season_hari"], y=season_usage["cnt_hari"], palette="viridis")
plt.xlabel("Musim")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Jumlah Rental Berdasarkan Jam")
hourly_usage = df.groupby("hr")["cnt_jam"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=hourly_usage["hr"], y=hourly_usage["cnt_jam"], color="blue")
plt.xlabel("Jam")
plt.ylabel("Total Rental")
st.pyplot(plt)

