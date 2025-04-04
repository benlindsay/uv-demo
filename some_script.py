# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "polars",
# ]
# ///

import polars as pl

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


if __name__ == "__main__":
    main()
