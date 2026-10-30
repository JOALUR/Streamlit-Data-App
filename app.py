from datetime import timedelta
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).parent / "data" / "water_quality_course.csv"

st.set_page_config(
    page_title="Water Quality Explorer",
    page_icon="💧",
    layout="wide",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load the course water-quality measurements."""
    data = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
    data["value"] = pd.to_numeric(data["value"], errors="coerce")
    return data.dropna(subset=["timestamp", "value"])


data = load_data()
measurements = sorted(data["measurement"].unique())
first_timestamp = data["timestamp"].min()
last_timestamp = data["timestamp"].max()

st.title("💧 Water Quality Explorer")
st.markdown(
    "Explore water-quality measurements from a course-provided survey. "
    "Choose a measurement and time window to see how its readings changed "
    "during the survey."
)
st.caption(
    "The chart and summaries describe the supplied sensor readings. "
    "They do not apply regulatory limits or assess water safety."
)

with st.sidebar:
    st.header("Explore the data")
    selected_measurement = st.selectbox("Measurement", measurements)
    selected_time = st.slider(
        "Time window",
        min_value=first_timestamp.to_pydatetime(),
        max_value=last_timestamp.to_pydatetime(),
        value=(
            first_timestamp.to_pydatetime(),
            last_timestamp.to_pydatetime(),
        ),
        step=timedelta(seconds=1),
        format="HH:mm:ss",
    )

filtered_data = data.loc[
    data["measurement"].eq(selected_measurement)
    & data["timestamp"].between(selected_time[0], selected_time[1])
].copy()

st.header("Overview")
if filtered_data.empty:
    st.info("No readings match this time window. Widen the time slider.")
else:
    unit = str(filtered_data["unit"].iloc[0])
    reading_count = len(filtered_data)
    average = filtered_data["value"].mean()
    minimum = filtered_data["value"].min()
    maximum = filtered_data["value"].max()

    metric_columns = st.columns(3)
    metric_columns[0].metric("Readings shown", reading_count)
    metric_columns[1].metric(f"Average ({unit})", f"{average:.2f}")
    metric_columns[2].metric(
        f"Observed range ({unit})",
        f"{minimum:.2f}–{maximum:.2f}",
    )

    st.header("Data display")
    chart = px.line(
        filtered_data,
        x="timestamp",
        y="value",
        color="measurement",
        markers=True,
        labels={
            "timestamp": "Time",
            "value": f"{selected_measurement} ({unit})",
            "measurement": "Water-quality measurement",
        },
        title=f"{selected_measurement} during the survey",
    )
    chart.update_layout(
        xaxis_title="Time on October 21, 2021",
        yaxis_title=f"{selected_measurement} ({unit})",
        legend_title_text="Water-quality measurement",
        hovermode="x unified",
    )
    st.plotly_chart(chart, use_container_width=True)

    st.header("Insights")
    st.write(
        f"The selected time window contains **{reading_count} readings** "
        f"for **{selected_measurement}**, from **{minimum:.2f}** to "
        f"**{maximum:.2f} {unit}**. These statistics describe this dataset "
        "only; consult the course's source and calibration information "
        "before interpreting the readings."
    )
    with st.expander("View filtered readings"):
        st.dataframe(
            filtered_data[["timestamp", "measurement", "value", "unit"]],
            hide_index=True,
            use_container_width=True,
        )

st.divider()
st.caption(
    "Only water-quality measurements are included in the app dataset; "
    "GPS coordinates and vehicle telemetry are excluded."
)
