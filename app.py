import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# add page options for overall app
ui.page_opts(title="🎉P1: Browers Interactive App🎉", fillable=True)

# Create a sidebar with slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in a hisogram. 
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Number of Bins") to be displayed alongside a slider.
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initual value of the slider
    ui.input_slider("selected_number_of_bins", "Number of Bins",0,100,20)

@render.plot(alt="A histogram showing random data distibution")
def draw_histogram():
    #define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 1000000
    #set a random seed to ensure reproducibility. 
    np.random.seed(1000)
    # Generate random data:
    # - np.random.randn(count_of_points) generates 'count_of_points' samples from a standard normal distribution.
    # Each sample is them scaled by 15 (to increase spread) and shifted by 100 (to center the distribution around 100).
    random_data_array = 100 + 15*np.random.randn(count_of_points)
    # Create a histogram of a random data using matplotlib's hist() function:
    # The second argument specifites the number of bins, dyamically set by the input sliders current value.
    # The desnifty parameter, when true, normalicses the histogram so that the total area under the histogram equals 1. 
    plt.hist(random_data_array, input.selected_number_of_bins(), density= True, color="red")
    plt.xlabel('Value')
    plt.ylabel('Frequency')
