# Water Quality Explorer

An interactive dashboard for exploring water-quality measurements from a
course-provided survey. Choose a measurement and time window to view its
readings, summary statistics, and interactive Plotly chart.

**Live app:** [Open Water Quality Explorer](https://app-data-appgit-xkxxtzxjunur5cbsqprplq.streamlit.app/)  
**GitHub repository:** [JOALUR/Streamlit-Data-App](https://github.com/JOALUR/Streamlit-Data-App)

## Dataset

The app uses [`data/water_quality_course.csv`](./data/water_quality_course.csv),
prepared from the course-provided `2021-oct21.csv`. It contains 3,159
water-quality readings from October 21, 2021, covering pH, turbidity,
chlorophyll, blue-green algae, dissolved oxygen, oxygen saturation, water
temperature, specific conductivity, and salinity. GPS and vehicle telemetry
from the original file are excluded.

The dashboard presents descriptive summaries only; it does not apply
regulatory thresholds or assess water safety. Interpret readings using the
course's source and calibration information.

## How to use

1. Open the live app.
2. Select a water-quality measurement from the sidebar.
3. Adjust the time-window slider to focus on part of the survey.
4. Explore the chart and summary metrics. Expand **View filtered readings**
   to inspect the data behind the chart.