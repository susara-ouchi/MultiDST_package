### Necessary libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

################################################################################################
#### Plot 01: Sigplot -> Heatplot with significant indices
def sigindex_plot(methods, sig_indices, title=None, save_plot=True,timestamp=""):
    """
    Generates a heatmap plot to visualize the indices of significant points selected by different methods.

    Parameters:
    - methods (list of str): A list of method names or condition labels.
    - sig_indices (list of list of int): A list of lists, where each sublist contains the indices of significant points for the corresponding method.
    - title (str, optional): The title of the plot. If not provided, a default title 'Selected Points by Methods' is used.
    - save_plot (bool, optional): If True, saves the plot as 'sigplot.png'. Default is True.
    """
    sig_indices = [i if i else [] for i in sig_indices]
    # Create a matrix to represent the selected points for each method
    max_index = max(max(indices) for indices in sig_indices if indices!=[])
    matrix = np.zeros((len(methods), max_index+1))

    # Fill the matrix with 1 where a method selected a point
    for i, indices in enumerate(sig_indices):
        for idx in indices:
            matrix[i, idx] = 1  # Subtract 1 to align with 0-based indexing

    # Plot the heatmap
    plt.figure(figsize=(9, 3))
    plt.imshow(matrix, cmap='Blues', aspect='auto', interpolation='nearest')

    # Customize the plot
    plt.xlabel('Hypothesis index', fontname='Times New Roman',fontsize=14)
    plt.ylabel('Method / Condition', fontname='Times New Roman',fontsize=14)
    if title:
        plt.title(title, fontname='Times New Roman')
    else:
        plt.title('Selected Points by Methods', fontname='Times New Roman', fontsize=14)
    plt.yticks(np.arange(len(methods)), methods)

    # Add a legend box
    legend_box = Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='none', facecolor='midnightblue', label='Significant')
    plt.legend(handles=[legend_box], loc='upper right')
    plt.tight_layout()
    
    if save_plot == True:
        plt.savefig(f'sigplot{timestamp}.png', bbox_inches='tight')
    # return plt.gca().figure
    plt.show()

########################################################################################################
#### Plot 02: Fire histogram

def multidst_hist(p_values, g2_index, title="plot",col1 = 'skyblue', col2 = 'skyblue', show_legend=False, left='firing',right='non-firing',timestamp=""):
      """
      Generates a histogram comparing two sets of p-values and saves the plot as an image file.

      Parameters:
      - p_values (list of float): The list of p-values to be divided into two groups.
      - g2_index (list of int): The list of indices indicating the non-firing group in p_values.
      - title (str): The title of the histogram plot. Default is "plot".
      - col1 (str): The color for the 'firing' group histogram bars. Default is 'skyblue'.
      - col2 (str): The color for the 'non-firing' group histogram bars. Default is 'skyblue'.
      - show_legend (bool): If True, display the legend on the plot. Default is False.
      - left (str): The label for the 'firing' group. Default is 'firing'.
      - right (str): The label for the 'non-firing' group. Default is 'non-firing'.
      """
      p_value_nonfire = [p_values[i] for i in g2_index]
      p_value_fire = [p_values[i] for i in range(len(p_values)) if i not in g2_index]

      hist_data = [p_value_fire, p_value_nonfire]
      plt.hist(hist_data, bins=30, alpha=1, label=[left, right], color=[col1, col2],
               edgecolor='black', stacked=True)
      plt.title(title, fontname='Times New Roman')
      plt.xlabel('p-value', fontname='Times New Roman')
      plt.ylabel('Frequency', fontname='Times New Roman')
      if show_legend == True:
        plt.legend()
      plt.savefig(f'hist{timestamp}.png', bbox_inches='tight')
      plt.show()
    # return plt.gca().figure



############################################################################################
####################### OTHER PLOTS (Optional) #############################################
############################################################################################

def draw_histogram(data, bins=10, color='skyblue', edgecolor='black', title='Histogram', xlabel='Values', ylabel='Frequency'):
    """
    Draw a histogram using user-defined function.

    Parameters:
        data (array-like): Input data for the histogram.
        bins (int or array, optional): Number of bins or bin edges. Default is 10.
        color (str, optional): Color of the bars. Default is 'skyblue'.
        edgecolor (str, optional): Color of the bar edges. Default is 'black'.
        title (str, optional): Title of the chart. Default is 'Histogram'.
        xlabel (str, optional): Label for the x-axis. Default is 'Values'.
        ylabel (str, optional): Label for the y-axis. Default is 'Frequency'.
    """
    plt.hist(data, bins=bins, color=color, edgecolor=edgecolor)

    # Customize the chart
    plt.title(title, fontname='Times New Roman', fontsize=15)
    plt.xlabel(xlabel,fontname='Times New Roman', fontsize=15)
    plt.ylabel(ylabel,fontname='Times New Roman', fontsize=15)

    # Show the chart
    plt.show()

#############################################################################################

def group_line_plot(df_select, g_var,var1,var2): 
    # Grouping the DataFrame by 'pi0'
    grouped = df_select.groupby(g_var)

    # Plotting each group separately
    for name, group in grouped:
        plt.plot(group[var1], group[var2], label=f'{g_var} = {name}')

    # Adding labels, title, and legend
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.title(f'Line Plot of {var2} over {var1}')
    plt.grid(True)
    plt.legend()
    plt.show()


###########################################################################################################
def draw_bar_chart(categories, values, title='Bar Chart', xlabel='Categories', ylabel='Values', border_color='grey'):
    """
    Draw a bar chart using user-defined function.

    Parameters:
        categories (list): List of category labels.
        values (list): List of corresponding values for each category.
        title (str): Title of the chart (default is 'Bar Chart').
        xlabel (str): Label for the x-axis (default is 'Categories').
        ylabel (str): Label for the y-axis (default is 'Values').
        border_color (str): Color of the borders (default is 'black').
    """
    colors = ['cornflowerblue', 'greenyellow']
    bars = plt.bar(categories, values, color=colors)
    
    # Add borders to bars
    for bar in bars:
        bar.set_edgecolor(border_color)
    
    plt.title(title, fontname='Times New Roman', fontsize=15)
    plt.xlabel(xlabel, fontname='Times New Roman', fontsize=15)
    plt.ylabel(ylabel, fontname='Times New Roman', fontsize=15)
    plt.xticks(fontname='Times New Roman', fontsize=15) 
    plt.show()

#######################################################################################################

def draw_p_bar_chart(categories, values, title='Bar Chart', xlabel='Type', ylabel='Values', border_color='grey'):
    """
    Draw a bar chart using user-defined function.

    Parameters:
        categories (list): List of category labels.
        values (list): List of corresponding values for each category.
        title (str): Title of the chart (default is 'Bar Chart').
        xlabel (str): Label for the x-axis (default is 'Categories').
        ylabel (str): Label for the y-axis (default is 'Values').
        border_color (str): Color of the borders (default is 'black').
    """
    colors = ['#3553ff', '#72ff35']
    bars = plt.bar(categories, values, color=colors)
    
    # Add borders to bars
    for bar in bars:
        bar.set_edgecolor(border_color)
    
    plt.title(title, fontname='Times New Roman',fontsize=15)
    plt.xlabel(xlabel, fontname='Times New Roman',fontsize=13)
    plt.ylabel(ylabel, fontname='Times New Roman', fontsize=13)
    plt.xticks(fontname='Times New Roman', fontsize=10)  # Set font for category labels
    
    # Adding percentage labels on bars with box
    total = sum(values)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        text = f'{height / total * 100:.2f}%'
        if i == 0:
            plt.text(bar.get_x() + bar.get_width() / 2, height/2, text, ha='center', va='center', color="black", fontname='Times New Roman', fontsize=15, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height+4, text, ha='center', va='bottom', color="black", fontname='Times New Roman', fontsize=15, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    
    plt.ylim(0,100)
    plt.yticks(range(0,101,10), fontsize=10)

    plt.show()

# # Example usage:
# categories = ['A', 'B']
# values = [40, 60]
# draw_p_bar_chart(categories, values, title='Percentage Bar Chart', ylabel='Percentage')

###############################################################################################################
