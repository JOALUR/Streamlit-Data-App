# Water Quality Explorer

An interactive Streamlit dashboard for exploring water-quality measurements
from a course-provided survey. Select a measurement and time window to view an
interactive Plotly time series, summary metrics, and the readings used for
those summaries.

## Dataset

The app uses [`data/water_quality_course.csv`](./data/water_quality_course.csv),
prepared from the course-provided `2021-oct21.csv`. It contains 3,159
water-quality readings from 351 timestamp records on October 21, 2021. The
included measurements are pH, turbidity, chlorophyll, blue-green algae,
dissolved oxygen, oxygen saturation, water temperature, specific conductivity,
and salinity.

The course source also contained GPS and vehicle/sensor telemetry. Those
unrelated fields have been excluded from the app dataset. The app summarizes
the recorded sensor values but does not apply regulatory thresholds or make a
water-safety assessment. Sensor readings can include outliers or instrument
artifacts; use course-provided source and calibration information when
interpreting them. Add the source attribution required by your course here
before publishing.

`data/water_quality.csv` is the synthetic starter example retained separately;
the app does not load it.

## Run locally

Python 3.10 or later is recommended.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually `http://localhost:8501`).
Use the sidebar to select a water-quality measurement and adjust the time
window. The chart, summary metrics, and expandable readings table update from
your selections.

## Project layout

```text
.
├── app.py
├── data/
│   ├── water_quality_course.csv
│   └── water_quality.csv  # retained synthetic example; not loaded by the app
├── requirements.txt
└── README.md
```

`requirements.txt` lists the app's Python dependencies. The course dataset is
bundled locally, so the app does not need an API key or secret.

## Agile process and evidence

Track work as small user stories on a board with **Backlog → Ready → In
Progress → Done**. At the end of each iteration, run the app, check the
acceptance criteria, review it from a user's perspective, and add an
improvement from the retrospective to the backlog.

| Priority | User story / acceptance criteria | Status |
|---|---|---|
| 1 | As a user, I can understand what the dashboard and dataset contain. | Done |
| 2 | As a user, I can select a water-quality measurement and time window. | Done |
| 3 | As a user, I can see a labeled Plotly chart with a title, axes, and legend. | Done |
| 4 | As a user, I can review summary metrics and filtered source readings. | Done |
| 5 | As a maintainer, I can install dependencies and follow deployment instructions. | Ready for review |

**Definition of Done:** acceptance criteria work in the running app; the
interface explains the data; dependencies and instructions are current; and
the change is checked locally before it is marked Done.

**Review / retrospective prompts:** Were the available measurements and
time-window control understandable? Did the chart help answer a question
about the survey? Record one concrete improvement as a backlog item.

## Publish and deploy

When you are ready, create or connect the repository using your own GitHub
account, then deploy the repository on Streamlit Community Cloud with `app.py`
as the main file. Check the public app's filters, chart, and data table after
deployment. Confirm your course's dataset attribution and sharing rules before
publishing.

**Live app:** _add your Streamlit Community Cloud URL after deployment_

**Repository:** _add your GitHub repository URL after publishing_
