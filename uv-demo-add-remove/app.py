import polars as pl
# import streamlit as st

# NY winning lottery numbers
# https://catalog.data.gov/dataset/lottery-mega-millions-winning-numbers-beginning-2002
# DATA_URL "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD"

# Hamonized Tariff Schedule
# https://catalog.data.gov/dataset/harmonized-tariff-schedule-of-the-united-states-2024
DATA_URL = (
    "https://www.usitc.gov/sites/default/files/tata/hts/hts_2025_revision_2_csv.csv"
)


def main():
    data = pl.read_csv(DATA_URL)
    print(data.shape)
    print(data.head())
    # st.set_page_config(layout="wide")
    # st.write(data)


if __name__ == "__main__":
    main()
