
# ------------------------------
# IMPORTS
# ------------------------------
import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="AirFly Insights Dashboard", layout="wide")

# ------------------------------
# DESIGN (DARK THEME)
# ------------------------------
# ------------------------------
# SIDEBAR FILTERS
# ------------------------------
# ------------------------------
# DARK THEME UI
# ------------------------------
st.markdown("""
<style>
/* Main page background */
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* All text white */
h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: white !important;
}

/* Tabs styling */
button[data-baseweb="tab"] {
    color: white !important;
    font-weight: bold;
}
/* Multiselect dropdown selected area */
div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #374151 !important;
}

/* Dropdown popup list background */
div[role="listbox"] {
    background-color: #111827 !important;
    color: white !important;
}

/* Each option inside dropdown */
div[role="option"] {
    background-color: #111827 !important;
    color: white !important;
}
/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}
            /* Multiselect dropdown box */
div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #4b5563 !important;
}

/* Selected chips */
div[data-baseweb="tag"] {
    background-color: #2563eb !important;
    color: white !important;
}

/* Dropdown menu options */
ul {
    background-color: #111827 !important;
    color: white !important;
}

li {
    color: white !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)



# ------------------------------
# LOAD DATA
# ------------------------------
df = pd.read_csv("Data/Processed/flights_2009_processed.csv")

# ------------------------------
# ADD LAT/LONG (MAP)
# ------------------------------
airport_coords = {
    "ATL": (33.6407, -84.4277),
    "LAX": (33.9416, -118.4085),
    "ORD": (41.9742, -87.9073),
    "DFW": (32.8998, -97.0403),
    "DEN": (39.8561, -104.6737),
    "JFK": (40.6413, -73.7781),
    "SFO": (37.6213, -122.3790),
    "SEA": (47.4502, -122.3088),
    "MIA": (25.7959, -80.2870),
    "PHX": (33.4373, -112.0078),
    "IAH": (29.9902, -95.3368),
    "LAS": (36.0840, -115.1537)
}

df["LATITUDE"] = df["ORIGIN"].map(lambda x: airport_coords.get(x, (None, None))[0])
df["LONGITUDE"] = df["ORIGIN"].map(lambda x: airport_coords.get(x, (None, None))[1])
df = df.dropna(subset=["LATITUDE", "LONGITUDE"])



# ------------------------------
# SIDEBAR FILTERS
# ------------------------------
st.sidebar.title("🔍 Filters")

selected_airline = st.sidebar.multiselect(
    "Select Airline",
    options=df["OP_CARRIER"].unique()
)

selected_month = st.sidebar.multiselect(
    "Select Month",
    options=df["MONTH"].unique()
)

delay_range = st.sidebar.slider(
    "Delay Range",
    int(df["DEP_DELAY"].min()),
    int(df["DEP_DELAY"].max()),
    (0, 100)
)

# ------------------------------
# APPLY FILTERS
# ------------------------------
filtered_df = df.copy()

if selected_airline:
    filtered_df = filtered_df[filtered_df["OP_CARRIER"].isin(selected_airline)]

if selected_month:
    filtered_df = filtered_df[filtered_df["MONTH"].isin(selected_month)]

filtered_df = filtered_df[
    (filtered_df["DEP_DELAY"] >= delay_range[0]) &
    (filtered_df["DEP_DELAY"] <= delay_range[1])
]

# ------------------------------
# TITLE
# ------------------------------
st.title("✈️ AirFly:Smart Airline Insights Dashboard")

# ------------------------------
# TABS
# ------------------------------
tab1, tab2, tab3 = st.tabs(["📊 Overview", "✈️ Flights", "⏱ Delays"])

# ==============================
# TAB 1 - OVERVIEW
# ==============================
with tab1:

    col1, col2, col3 = st.columns(3)

    col1.metric("✈️ Total Flights", len(filtered_df))
    col2.metric("⏱ Avg Delay", round(filtered_df["DEP_DELAY"].mean(), 2))
    col3.metric("❌ Cancelled", int(filtered_df["CANCELLED"].sum()))

    st.subheader("🌍 Flight Distribution Across Airports")

    map_data = filtered_df.groupby(
        ["ORIGIN", "LATITUDE", "LONGITUDE"]
    ).size().reset_index(name="Flights")

    fig_map = px.scatter_mapbox(
        map_data,
        lat="LATITUDE",
        lon="LONGITUDE",
        size="Flights",
        hover_name="ORIGIN",
        zoom=4
    )

    fig_map.update_layout(
        mapbox_style="carto-darkmatter",
        mapbox_center={"lat": 39, "lon": -98}
    )

    st.plotly_chart(fig_map, use_container_width=True)

    with st.expander("📊 View Dataset"):
        st.write(filtered_df.head())
        



# ==============================
# TAB 2 - FLIGHTS
# ==============================
with tab2:

    filtered_df["ROUTE"] = filtered_df["ORIGIN"] + "-" + filtered_df["DEST"]

    st.subheader("Top 10 Busiest Routes")

    top_routes = filtered_df["ROUTE"].value_counts().head(10)

    fig_routes = px.bar(
        x=top_routes.values,
        y=top_routes.index,
        orientation='h'
    )

    st.plotly_chart(fig_routes, use_container_width=True)

    st.subheader("Top Airports")

    top_airports = filtered_df["ORIGIN"].value_counts().head(10)

    fig_airports = px.bar(
        x=top_airports.values,
        y=top_airports.index,
        orientation='h'
    )

    st.plotly_chart(fig_airports, use_container_width=True)

    st.subheader("Flights by Departure Hour")

    hour_data = filtered_df['DEP_HOUR'].value_counts().sort_index().reset_index()
    hour_data.columns = ["Hour", "Flights"]

    fig_hour = px.line(
        hour_data,
        x="Hour",
        y="Flights",
        markers=True,
        title="Flight Distribution by Hour"
    )

    st.plotly_chart(fig_hour, use_container_width=True)

    st.subheader("Top Destination Airports")

dest_airports = filtered_df["DEST"].value_counts().head(10).reset_index()
dest_airports.columns = ["Destination", "Flights"]

fig_dest = px.bar(
    dest_airports,
    x="Destination",
    y="Flights",
    title="Top Destination Airports"
)

st.plotly_chart(fig_dest, use_container_width=True)

st.subheader("Best Time to Travel")

best_time = (
    filtered_df.groupby("DEP_HOUR")["DEP_DELAY"]
    .mean()
    .sort_values()
    .head(5)
    .reset_index()
)

fig = px.line(
    best_time,
    x="DEP_HOUR",
    y="DEP_DELAY",
    markers=True,
    title="Best Departure Hours with Lowest Delay"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("Recommended Airports (Least Congestion)")

least_busy = (
    filtered_df["ORIGIN"].value_counts()
    .sort_values()
    .head(5)
    .reset_index()
)
least_busy.columns = ["Airport", "Flights"]

fig = px.bar(
    least_busy,
    x="Airport",
    y="Flights",
    title="Least Congested Airports"
)

st.plotly_chart(fig, use_container_width=True)


# ==============================
# TAB 3 - DELAYS
# ==============================
with tab3:

    st.subheader("Monthly Cancellations")

    cancel_month = filtered_df.groupby("MONTH")["CANCELLED"].sum().reset_index()

    fig_line = px.line(
        cancel_month,
        x="MONTH",
        y="CANCELLED",
        markers=True
    )

    st.plotly_chart(fig_line, use_container_width=True)
    st.subheader("Recommended Airlines (Lowest Average Delay)")

    best_airlines = (
    filtered_df.groupby("OP_CARRIER")["DEP_DELAY"]
    .mean()
    .sort_values()
    .head(5)
    .reset_index()
    )

    fig = px.bar(
    best_airlines,
    x="OP_CARRIER",
    y="DEP_DELAY",
    title="Top 5 Recommended Airlines"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Cancellation Reasons")

    cancel_reason = filtered_df[
        filtered_df['CANCELLED'] == 1
    ]['CANCELLATION_CODE'].value_counts()

    fig_pie = px.pie(
        values=cancel_reason.values,
        names=cancel_reason.index
    )

    st.plotly_chart(fig_pie, use_container_width=True)
    st.subheader("Delay vs Month ")

    delay_month = filtered_df.groupby("MONTH")["DEP_DELAY"].mean().reset_index()

    fig = px.line(delay_month, x="MONTH", y="DEP_DELAY", markers=True)

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Delay Spread by Airline")

    fig = px.box(filtered_df, x="OP_CARRIER", y="DEP_DELAY")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Delay Heatmap")

    pivot = filtered_df.pivot_table(
        values="ARR_DELAY",
        index="OP_CARRIER",
        columns="MONTH",
        aggfunc="mean"
    )

    fig_heatmap = px.imshow(pivot, text_auto=True)
    st.plotly_chart(fig_heatmap, use_container_width=True)
    st.subheader("Departure Delay vs Arrival Delay")

    fig = px.scatter(
    filtered_df,
    x="DEP_DELAY",
    y="ARR_DELAY",
    opacity=0.5
)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Delay Distribution")

    fig_hist = px.histogram(
        filtered_df,
        x="DEP_DELAY",
        nbins=50,
        title="Distribution of Departure Delays"
    )

    st.plotly_chart(fig_hist, use_container_width=True)
    
    # ------------------------------
    # ON-TIME VS DELAYED FLIGHTS
    # ------------------------------
    st.subheader("On-Time vs Delayed Flights")

    st.write("""
    This chart compares flights that departed on time versus flights that experienced delays.
    It helps evaluate overall airline service reliability.
    """)

    filtered_df["FLIGHT_STATUS"] = filtered_df["DEP_DELAY"].apply(
    lambda x: "Delayed" if x > 0 else "On Time"
    )

    status_count = filtered_df["FLIGHT_STATUS"].value_counts().reset_index()
    status_count.columns = ["Status", "Flights"]

    fig_status = px.pie(
    status_count,
    values="Flights",
    names="Status",
    title="Flight Status Distribution"
)

    st.plotly_chart(fig_status, use_container_width=True)
    st.subheader("Weather Risk by Month")

    weather_risk = (
    filtered_df.groupby("MONTH")["WEATHER_DELAY"]
    .mean()
    .reset_index()
    )

    fig = px.line(
    weather_risk,
    x="MONTH",
    y="WEATHER_DELAY",
    markers=True,
    title="Weather Delay Trend"
    )

    st.plotly_chart(fig, use_container_width=True)
    # ------------------------------
    # SEASONAL DELAY ANALYSIS
    # ------------------------------
    st.subheader("Seasonal Delay Analysis")

    season_delay = filtered_df.groupby("SEASON")["DEP_DELAY"].mean().reset_index()

    fig_season = px.bar(
    season_delay,
    x="SEASON",
    y="DEP_DELAY",
    title="Average Departure Delay by Season"
    )

    st.plotly_chart(fig_season, use_container_width=True)

    st.subheader("Average Delay by Airline")

    delay_airline = filtered_df.groupby("OP_CARRIER")["DEP_DELAY"].mean().sort_values(ascending=False).head(10).reset_index()

    fig_airline_delay = px.bar(
        delay_airline,
        x="OP_CARRIER",
        y="DEP_DELAY",
        title="Top Airlines by Average Delay"
    )

    st.plotly_chart(fig_airline_delay, use_container_width=True)
    st.subheader("Cancellation Trend by Reason")

    cancel_reason_month = filtered_df.groupby(
    ["MONTH", "CANCELLATION_CODE"]
    ).size().reset_index(name="Count")

    fig = px.line(
    cancel_reason_month,
    x="MONTH",
    y="Count",
    color="CANCELLATION_CODE",
    markers=True
    )

    st.plotly_chart(fig, use_container_width=True)
    

# ------------------------------
# DOWNLOAD BUTTON
# ------------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    "⬇️ Download Filtered Data",
    csv,
    "filtered_data.csv",
    "text/csv"
)

# ------------------------------
# INSIGHTS
# ------------------------------
st.header("📌 Key Insights")

st.write("""
* Major airports act as aviation hubs  
* Weather & carrier issues cause cancellations  
* Delay trends vary across months  
* Peak traffic routes dominate airline operations  
""")