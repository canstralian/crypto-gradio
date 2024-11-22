import gradio as gr
from logic import (
    load_data, data_summary, plot_data,
    calculate_statistics, perform_t_test,
    get_bybit_data, get_tradingview_data
)

# Load data
file_path = "path/to/your/data.csv"
data = load_data(file_path)

# Define functions for Gradio interface
def summary():
    return data_summary(data)

def plot():
    plot_data(data)

def stats():
    return calculate_statistics(data)

def t_test():
    return perform_t_test(data)

def bybit_data():
    return get_bybit_data()

def tradingview_data():
    return get_tradingview_data()

# Create Gradio interface
summary_interface = gr.Interface(fn=summary, inputs=None, outputs="text", title="Data Summary")
plot_interface = gr.Interface(fn=plot, inputs=None, outputs=None, title="Data Plot")
stats_interface = gr.Interface(fn=stats, inputs=None, outputs="text", title="Data Statistics")
t_test_interface = gr.Interface(fn=t_test, inputs=None, outputs="text", title="T-Test Results")
bybit_interface = gr.Interface(fn=bybit_data, inputs=None, outputs="text", title="Get Bybit Data")
tradingview_interface = gr.Interface(fn=tradingview_data, inputs=None, outputs="text", title="Get TradingView Data")

# Launch Gradio interfaces
summary_interface.launch()
plot_interface.launch()
stats_interface.launch()
t_test_interface.launch()
bybit_interface.launch()
tradingview_interface.launch()