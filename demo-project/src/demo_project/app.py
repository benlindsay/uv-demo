import streamlit as st

from demo_project.data import get_counties, get_unemployment_data
from demo_project.plots import generate_map


def render_app():
    counties = get_counties()
    unemployment_data = get_unemployment_data()
    fig = generate_map(data=unemployment_data, counties=counties)

    st.title("US Unemployment Data by County")
    st.markdown(
        """
        This app visualizes the unemployment data in the United States by county.
        The data is sourced from Plotly's GitHub repository.
        """
    )
    st.write(fig)


if __name__ == "__main__":
    render_app()
