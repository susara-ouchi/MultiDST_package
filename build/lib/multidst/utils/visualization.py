### Necessary libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


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

##############################################################################

def plot_roc(methods, tpr_list, fpr_list):
    plt.figure(figsize=(8, 6))
    for i in range(len(methods)):
        plt.plot(fpr_list[i], tpr_list[i], label=methods[i])
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Random Guess')
    plt.xlabel('False Positive Rate (FPR)', fontname='Times New Roman')
    plt.ylabel('True Positive Rate (TPR)', fontname='Times New Roman')
    plt.title('Receiver Operating Characteristic (ROC) Curve', fontname='Times New Roman')
    plt.legend()
    plt.grid(True)
    plt.show()

# # Example data for TPR and FPR for 7 different methods
# methods = ['Method 1', 'Method 2', 'Method 3', 'Method 4', 'Method 5', 'Method 6', 'Method 7']
# tpr_list = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#             [0.15, 0.35, 0.55, 0.75, 0.85], [0.25, 0.45, 0.65, 0.8, 0.95], [0.1, 0.2, 0.3, 0.4, 0.5],
#             [0.05, 0.1, 0.15, 0.2, 0.25]]
# fpr_list = [[0.1, 0.2, 0.3, 0.4, 0.5], [0.15, 0.25, 0.35, 0.45, 0.55], [0.05, 0.15, 0.25, 0.35, 0.45],
#             [0.1, 0.2, 0.3, 0.4, 0.5], [0.08, 0.18, 0.28, 0.38, 0.48], [0.05, 0.1, 0.15, 0.2, 0.25],
#             [0.01, 0.05, 0.1, 0.15, 0.2]]

# plot_roc(methods, tpr_list, fpr_list)


#########################################################################################

def plot_power_effect(methods, effect_sizes, powers_s0, powers_s1, powers_s2=None, titles=None, x_labels=None, y_labels=None):
    num_plots = 2 if powers_s2 is None else 3
    plt.figure(figsize=(5*num_plots, 5))

    # Define colors and markers
    colors = ['black', 'red', 'purple', 'tomato', 'mediumseagreen', 'navy', 'magenta']
    markers = ['o', 's', '^', 'v', 'D', '*','X']

    # Plot for s = 0.5 / n = 5
    plt.subplot(1, num_plots, 1)
    for i in range(len(methods)):
        plt.plot(effect_sizes, powers_s0[i], label=methods[i], color=colors[i % len(colors)], marker=markers[i % len(markers)])
    plt.xlabel(x_labels[0] if x_labels else 'Effect Size', fontname='Times New Roman')
    plt.ylabel(y_labels[0] if y_labels else 'Power', fontname='Times New Roman')
    plt.title(titles[0] if titles else 'Power vs. Effect Size (S0 = 0.5)', fontname='Times New Roman')
    plt.ylim(0, 1.0)  # Set y-axis limits
    plt.legend(loc='upper left', prop={'family': 'Times New Roman'})
    plt.grid(True)

    # Plot for S = 1.0 / n = 15
    plt.subplot(1, num_plots, 2)
    for i in range(len(methods)):
        plt.plot(effect_sizes, powers_s1[i], label=methods[i], color=colors[i % len(colors)], marker=markers[i % len(markers)])
    plt.xlabel(x_labels[1] if x_labels else 'Effect Size', fontname='Times New Roman')
    plt.ylabel(y_labels[1] if y_labels else 'Power', fontname='Times New Roman')
    plt.title(titles[1] if titles else 'Power vs. Effect Size (S1 = 1.0)', fontname='Times New Roman')
    plt.ylim(0, 1.0)  # Set y-axis limits
    plt.grid(True)

    # Plot for n = 30 
    if num_plots == 3:
        plt.subplot(1, num_plots, 3)
        for i in range(len(methods)):
            plt.plot(effect_sizes, powers_s2[i], label=methods[i], color=colors[i % len(colors)], marker=markers[i % len(markers)])
        plt.xlabel(x_labels[2] if x_labels else 'Effect Size', fontname='Times New Roman')
        plt.ylabel(y_labels[2] if y_labels else 'Power', fontname='Times New Roman')
        plt.title(titles[2] if titles else 'Power vs. Effect Size (S2 = 1.5)', fontname='Times New Roman')
        plt.ylim(0, 1.0)  # Set y-axis limits
        plt.grid(True)

    plt.tight_layout()
    plt.show()




# # Example data for effect sizes and powers for 7 different methods
# methods = ['Method 1', 'Method 2', 'Method 3', 'Method 4', 'Method 5', 'Method 6', 'Method 7']
# effect_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]
# powers_s0 = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#              [0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0]]
# powers_s1 = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#              [0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0]]

# titles =['Custom Title 1', 'Custom Title 2', 'Custom Title 3']
# x_labels = ['Effect size','Effect size','Effect size']
# y_labels = ['Power','Power','Power']
# plot_power_effect(methods, effect_sizes, powers_s0, powers_s1, titles=titles)


# # For the n plot
# methods = ['Method 1', 'Method 2', 'Method 3', 'Method 4', 'Method 5', 'Method 6', 'Method 7']
# effect_sizes = [0.1, 0.2, 0.3, 0.4, 0.5]
# powers_n0 = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#              [0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0]]
# powers_n1 = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#              [0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0]]
# powers_n2 = [[0.2, 0.4, 0.6, 0.8, 1.0], [0.3, 0.5, 0.7, 0.85, 0.95], [0.1, 0.3, 0.5, 0.75, 0.9],
#              [0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0],[0.2, 0.4, 0.6, 0.8, 1.0]]

# titles =['Custom Title 1', 'Custom Title 2', 'Custom Title 3']
# plot_power_effect(methods, effect_sizes, powers_n0, powers_n1, powers_n2, titles=titles)

###############################################################################################################

## Heatplot with sig indices
def sigindex_plot(methods, sig_indices, title=None):
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
    plt.show()

    # return plt.gca().figure


# Example usage
methods = ['Bonferroni', 'Holm', 'SGoF', 'BH', 'BY', 'Q value']
# sig_indices = [sig_bonf_p, sig_holm_p, sig_sgof_p, sig_bh_p, sig_by_p, sig_q]
sig_indices = [[0,1],[1,2,10],[1,2,14],[0,2],[1,2,13],[1,2,8]]
# sig_indices = [[0,1,2,3],[2,5],[],[],[1],[]]
# sigindex_plot(methods, sig_indices, title="New Title")

########################################################################################################

# Fire histogram

def multidst_hist(p_values, g2_index, title="plot",col1 = 'skyblue', col2 = 'skyblue',left='firing',right='non-firing'):
      p_value_nonfire = [p_values[i] for i in g2_index]
      p_value_fire = [p_values[i] for i in range(len(p_values)) if i not in g2_index]

      hist_data = [p_value_fire, p_value_nonfire]
      plt.hist(hist_data, bins=30, alpha=1, label=[left, right], color=[col1, col2],
               edgecolor='black', stacked=True)
      plt.title(title, fontname='Times New Roman')
      plt.xlabel('p-value', fontname='Times New Roman')
      plt.ylabel('Frequency', fontname='Times New Roman')
      plt.legend()
      plt.show()

    #   return plt.gca().figure

p_values = [0.1,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
g2_index = [2,5,9,10]
multidst_hist(p_values,g2_index, title="Histogram",col1 = 'skyblue', col2 = 'purple',left='firing',right='non-firing')
