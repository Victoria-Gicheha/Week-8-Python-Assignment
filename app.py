import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("CORD-19 Data Explorer")
st.write("A simple Streamlit app to explore COVID-19 research papers metadata.")

# Load dataset (adjust path if needed)
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    # Clean a bit
    df = df.dropna(subset=["title", "abstract", "publish_time"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Show a sample of the data
st.subheader("Sample Data")
st.dataframe(df.head(10))

# Slider for year selection
year_range = st.slider(
    "Select publication year range",
    int(df["year"].min()),
    int(df["year"].max()),
    (2020, 2021)
)

# Filter data by year range
df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Plot publications per year
st.subheader("Publications per Year")
counts = df_filtered["year"].value_counts().sort_index()

fig, ax = plt.subplots()
counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)
