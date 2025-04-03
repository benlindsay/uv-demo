import httpx
import pandas as pd


def get_counties():
    """
    Fetches the GeoJSON data for US counties from Plotly's GitHub repository.

    Returns:
        httpx.Response: The response object containing the GeoJSON data.
    """
    response = httpx.get(
        "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
    )
    return response.json()


def get_unemployment_data():
    return pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
        dtype={"fips": str},
    )
