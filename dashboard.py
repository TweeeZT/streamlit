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


selected_year = st.sidebar.multiselect("Pilih Tahun", df["yr_hari"].unique(), default=df["yr_hari"].unique())
selected_season = st.sidebar.multiselect("Pilih Musim", df["season_hari"].unique(), default=df["season_hari"].unique())

df_filtered = df[(df["yr_hari"].isin(selected_year)) & (df["season_hari"].isin(selected_season))]


base_color = "Blues"

st.subheader("Total Rental Berdasarkan Hari")
day_usage = df_filtered.groupby("weekday_hari")["cnt_hari"].sum().reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x=day_usage["weekday_hari"], y=day_usage["cnt_hari"], palette=base_color)
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Perbandingan Rental antara Workday dan Weekend")
workday_vs_weekend = df_filtered.groupby("workingday_hari")["cnt_hari"].sum().reset_index()
plt.figure(figsize=(6, 4))
sns.barplot(x=workday_vs_weekend["workingday_hari"], y=workday_vs_weekend["cnt_hari"], palette=base_color)
plt.xlabel("Kategori Hari")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Total Penyewaan Berdasarkan Musim")
season_usage = df_filtered.groupby("season_hari")["cnt_hari"].sum().reset_index()
plt.figure(figsize=(8, 4))
sns.barplot(x=season_usage["season_hari"], y=season_usage["cnt_hari"], palette=base_color)
plt.xlabel("Musim")
plt.ylabel("Total Rental")
st.pyplot(plt)

st.subheader("Jumlah Rental Berdasarkan Jam")
hourly_usage = df_filtered.groupby("hr")["cnt_jam"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x=hourly_usage["hr"], y=hourly_usage["cnt_jam"], palette=base_color)
plt.xlabel("Jam")
plt.ylabel("Total Rental")
st.pyplot(plt)
