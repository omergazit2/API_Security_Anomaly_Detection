import polars as pl
import plotly.express as px

def count_histogram(df: pl.DataFrame, x: str, title: str, x_title: str = None, y_title:str = None, ) -> None:
    """ creates a bar plot using plotly
    Args:
        df (pl.DataFrame): the dataframe to create the plot from
        x (str): the column to use for the x axis
        y (str): the column to use for the y axis
        title (str): the title of the plot
    Returns:
        None
    """
    fig = px.histogram(df, x = x, width = 600, height = 400)
    fig.update_layout(
        title=title,
        xaxis_title=x_title if x_title else x,
        yaxis_title=y_title if y_title else "count",
        template="plotly_white"
    )
    return fig