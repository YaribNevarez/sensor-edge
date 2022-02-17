import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

#Python:
begin   = np.array([0.000, 0.036, 64.496, 369.918, 394.903, 541.335, 553.404, 557.959, 565.621, 688.953, 694.984, 695.484, 725.975, 726.059, ])
latency = np.array([726.068, 64.060, 305.419, 24.192, 146.430, 12.066, 4.553, 4.531, 123.329, 6.029, 0.498, 30.486, 0.082, 0.008, ])
event   = ["Interpreter", "CONV_HW", "CONV_HW", "MAX_POOL_2D", "CONV_HW", "MAX_POOL_2D", "MUL", "ADD", "CONV_HW", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", ]
colors  = ["#1864ab", "#94c4df", "#94c4df", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", ]

data = [[0.003, 64.099, 369.918, 394.113, 541.335, 553.404, 557.959, 562.493, 688.953, 694.984, 695.484, 725.975, 726.059, ],
        [ 64.093, 305.817, 24.192, 147.220, 12.066, 4.553, 4.531, 126.458, 6.029, 0.498, 30.486, 0.082, 0.008, ],
        [ 64.060, 305.419, 0.000, 146.430, 0.000, 0.000, 0.000, 123.329, 0.000, 0.000, 0.000, 0.000, 0.000, ]]
columns = ("CONV_2D", "CONV_2D", "MAX_POOL_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", )

ax1.barh(range(len(begin)),  latency, left=begin, color=colors)
ax1.grid(linestyle = ':')


plt.sca(ax1)
plt.yticks(range(len(begin)), event)
ax1.tick_params(axis='both', which='major', labelsize=5)
ax1.tick_params(axis='both', which='minor', labelsize=1)

plt.xlabel("Schedule (ms)")
plt.ylabel("Task")

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