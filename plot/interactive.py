from data.download import download_data
import plotly.express as px


def plot_line_i(ticker:str):
    """ Plot a interactive plot using plotnine.

    Args:
        ticker (str): The ticker of financial asset.

    Returns:
        ggplot: A ticker interactive plot.
    """

    data = download_data(ticker)

    fig = px.line(
        data.reset_index(),
        x = 'Date', y = 'Close', title=ticker,
        labels={'Close': 'Fechamento', 'Date': 'Data'}
    )

    return fig