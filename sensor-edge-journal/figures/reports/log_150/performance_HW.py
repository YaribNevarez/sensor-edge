import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

begin   = np.array([0.000, 0.002, 0.012, 1.381, 1.390, 21.601, 45.642, 45.656, 51.914, 51.964, 64.235, 70.258, 72.546, 74.821, 75.219, 92.109, 93.615, 93.741, 94.346])
latency = np.array([94.353, 1.376, 1.366, 20.219, 20.209, 24.038, 6.270, 6.255, 12.319, 12.268, 6.021, 2.286, 2.273, 17.285, 16.887, 1.505, 0.124, 0.602, 0.006])
event   = ["Interpreter", "DEPTHWISE_CONV_2D", "CONV_HW", "CONV_2D", "CONV_HW", "MAX_POOL_2D", "DEPTHWISE_CONV_2D", "CONV_HW", "CONV_2D", "CONV_HW", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "CONV_HW", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX"]
colors = ["#1864ab", "#4a98c9", "#94c4df", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#94c4df", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9"]


ax1.barh(range(len(begin)),  latency, left=begin, color=colors)
ax1.grid(linestyle = ':')


plt.sca(ax1)
plt.yticks(range(len(begin)), event)
ax1.tick_params(axis='both', which='major', labelsize=5)
ax1.tick_params(axis='both', which='minor', labelsize=1)

plt.xlabel("Schedule (ms)")
plt.ylabel("Task")

data = [[ 0.002, 1.381, 21.601, 45.642, 51.914, 64.235, 70.258, 72.546, 74.821, 92.109, 93.615, 93.741, 94.346],
        [ 1.376, 20.219, 24.038, 6.270, 12.319, 6.021, 2.286, 2.273, 17.285, 1.505, 0.124, 0.602, 0.006],
        [ 1.366, 20.209, 0.000, 6.255, 12.268, 0.000, 0.000, 0.000, 16.887, 0.000, 0.000, 0.000, 0.000]]

columns = ("DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX")
rows = ["Hardware", "Software", "II OFFSET"]

# Get some pastel shades for the colors
colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    ax2.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(data[row])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

plt.sca(ax2)
# Add a table at the bottom of the axes
the_table = ax2.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom',
                      fontsize='xx-small')

the_table.auto_set_font_size(False)
the_table.set_fontsize(7)


# Adjust layout to make room for the table:

plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Latency (ms)")

plt.xticks([])
ax2.grid(linestyle = ':')


plt.show()