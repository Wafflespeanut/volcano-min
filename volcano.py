import matplotlib.pyplot as plt

OFFSET = 0.05   # offset for axis limits
Y_UPPER = 2.0   # upper limit for Y (up to which we're planning to hard-code)

with open('voldat.csv', 'r') as fd:
    data = map(lambda line: line.split(',')[1:3], fd.readlines())[1:]

x, y = zip(*map(lambda (x, y): (float(x), float(y)), data))
min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)

fig, ax = plt.subplots()

ax.set_xlim([min_x - OFFSET, max_x + OFFSET])
ax.set_ylim([min_y, max_y + OFFSET])
ax.scatter(x, y)

fig.set_size_inches(10, 7)      # no way to set 'resolution' for the image
ax.plot((min_x - OFFSET, max_x + OFFSET), (Y_UPPER, Y_UPPER))

min_x_pos = x.index(min_x)          # sample point (we choose the minimum for now)
pts = (x[min_x_pos], y[min_x_pos])
pts_disp = ax.transData.transform(pts)          # get the pixels corresponding to the point
width, height = fig.canvas.get_width_height()
print pts, pts_disp[0], height - pts_disp[1]    # since we'll need the height from top

fig.savefig('plot.png', dpi=fig.dpi)
