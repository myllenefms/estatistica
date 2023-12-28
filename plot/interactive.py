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
    data['SMA'] = data['Close'].rolling(window = 9).mean()
    data['LMA'] = data['Close'].rolling(window=72).mean()

    fig = px.line (
        data.reset_index(),
        x='Date',
        y=['Close', 'SMA', 'LMA'],
        labels={'Close': 'Fechamento', 'Date': 'Data'},
        color_discrete_map= 
        {'Close' : 'black', 'SMA' :'blue', 'LMA': 'red'}
    )
    
    return fig