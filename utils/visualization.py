import polars as pl
import plotly.express as px

def bar_plot(df: pl.DataFrame, x: str, y: str, title: str) -> None:
    """ creates a bar plot using plotly
    Args:
        df (pl.DataFrame): the dataframe to create the plot from
        x (str): the column to use for the x axis
        y (str): the column to use for the y axis
        title (str): the title of the plot
    Returns:
        None
    """
    fig = px.bar(df, x=x, title=title)
    fig.show()