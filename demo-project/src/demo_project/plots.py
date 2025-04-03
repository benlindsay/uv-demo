import pandas as pd
import plotly.express as px


def generate_map(data: pd.DataFrame, counties: dict):
    fig = px.choropleth(
        data,
        geojson=counties,
        locations="fips",
        color="unemp",
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        scope="usa",
        labels={"unemp": "unemployment rate"},
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig
