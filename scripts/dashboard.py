import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly as px
import os

directory = 'C:\\Users\\Melat\\Solar-Radiation-Measurement-Data-Analysis\\Data'
filename1 = 'benin-malanville.csv'
filename2 = 'sierraleone-bumbuna.csv'
filename3 = 'benin-malanville.csv'
file_path1 = os.path.join(directory, filename1)
file_path2 = os.path.join(directory, filename2)
file_path3 = os.path.join(directory, filename3)
#load data
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)
df3=  pd.read_csv(file_path3)
# Combine the datasets
dfs = [df1, df2, df3]
df = pd.concat(dfs, ignore_index=True)
# Convert the index to a DatetimeIndex
df = df.set_index('Timestamp')
df.index = pd.to_datetime(df.index)
# EDA
st.title("Exploratory Data Analysis")
# Summary Statistics
st.subheader("Summary Statistics")
summary_stats = df.describe()
st.write(summary_stats)
# Data Quality Check
st.subheader("Data Quality Check")
st.write("Missing Values:")
st.write(df.isnull().sum())
st.write("Negative values in GHI, DNI, and DHI:")
st.write(df[['GHI', 'DNI', 'DHI']][df[['GHI', 'DNI', 'DHI']] < 0].head())

st.write("Outliers in sensor readings and wind speed:")
z_scores = np.abs((df[['ModA', 'ModB', 'WS', 'WSgust']] - df[['ModA', 'ModB', 'WS', 'WSgust']].mean()) / df[['ModA', 'ModB', 'WS', 'WSgust']].std())
outliers = df[['ModA', 'ModB', 'WS', 'WSgust']][z_scores > 3].head()
st.write(outliers)
# Time Series Analysis
st.subheader("Time Series Analysis")
fig, ax = plt.subplots(figsize=(12, 8))
df[['GHI', 'DNI', 'DHI', 'Tamb']].plot(ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Values")
ax.set_title("Time Series of GHI, DNI, DHI, and Tamb")
st.pyplot(fig)

# Correlation Analysis
st.subheader("Correlation Analysis")
corr_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust']].corr()
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd', ax=ax)
ax.set_title("Correlation Heatmap")
st.pyplot(fig)

# Temperature and Humidity Analysis
st.subheader("Temperature and Humidity Analysis")
fig, ax = plt.subplots(figsize=(12, 8))
df.plot(y=['Tamb', 'RH'], ax=ax)
ax.set_xlabel("Timestamp")
ax.set_ylabel("Values")
ax.set_title("Ambient Temperature and Relative Humidity")
st.pyplot(fig)

# Temperature Analysis
st.subheader("Temperature Analysis")
fig, ax = plt.subplots(figsize=(12, 8))
df.plot(y=['Tamb', 'RH'], ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Values")
ax.set_title("Ambient Temperature and Relative Humidity")
st.pyplot(fig)


# Histograms
st.subheader("Histograms")
fig, axes = plt.subplots(2, 3, figsize=(16, 8))
df['GHI'].hist(ax=axes[0, 0])
df['DNI'].hist(ax=axes[0, 1])
df['DHI'].hist(ax=axes[0, 2])
df['WS'].hist(ax=axes[1, 0])
df['Tamb'].hist(ax=axes[1, 1])
df['RH'].hist(ax=axes[1, 2])
fig.suptitle("Histograms of Key Variables")
st.pyplot(fig)

# Bubble Chart
st.subheader("Bubble Chart")
fig = plt.figure(figsize=(12, 8))
sc = plt.scatter(df['GHI'], df['Tamb'], c=df['WS'], s=df['RH'] * 10, alpha=0.7)
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.title('Bubble Chart: GHI vs. Tamb vs. WS (Bubble size represents RH)')
plt.colorbar(sc, label='Wind Speed (WS)')
plt.legend(title='Relative Humidity (RH)')
plt.tight_layout()
st.pyplot(fig)
