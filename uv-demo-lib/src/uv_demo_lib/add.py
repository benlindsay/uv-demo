import polars as pl


def add_one(df: pl.DataFrame, col1: str) -> pl.DataFrame:
    """
    Add 1 to the values in the specified column of the DataFrame.

    Args:
        df (pl.DataFrame): Input DataFrame.
        col1 (str): Column name to add 1 to.

    Returns:
        pl.DataFrame: DataFrame with updated values in the specified column.
    """
    return df.with_columns((pl.col(col1) + 1).alias(col1))
