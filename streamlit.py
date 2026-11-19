
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🗳️ 2026 Governor Election Explorer")

# Load election results
url = "https://www.callthemap.com/results/data/2026/races.csv"
data = pd.read_csv(url)

# Select governor races
governors = data[data["office"] == "Governor"]

# Find winners or current leaders
winners = governors[governors["outcome"].isin(["won", "leads"])]
winners = winners.drop_duplicates(subset="state")

# Map election results
fig = px.choropleth(
    winners,
    locations="state",
    locationmode="USA-states",
    color="party",
    color_discrete_map={"D": "blue", "R": "red", "I": "purple"},
    hover_name="candidate",
    scope="usa",
    title="2026 Governor Election Results"
)

st.plotly_chart(fig, use_container_width=True)

# Explore individual states
state = st.selectbox(
    "Select a state",
    sorted(governors["state"].unique())
)

st.subheader(f"Results for {state}")

st.dataframe(
    governors[governors["state"] == state][
        ["candidate", "party", "votes", "share_pct"]
    ],
    hide_index=True
)
