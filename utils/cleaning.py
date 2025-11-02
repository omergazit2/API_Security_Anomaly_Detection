import polars as pl

def count_missing_values(df: pl.DataFrame) -> pl.DataFrame:
    """ returns a dataframe with the count of missing values for each column
    Args:
        df (pl.DataFrame): the dataframe to count the missing values of
    Returns:
        pl.DataFrame: a dataframe with the count of missing values for each column
    """
    return df.select(pl.col(c).is_null().sum().alias(f"{c}_missing") for c in df.columns)

