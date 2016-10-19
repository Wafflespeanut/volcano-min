## volcano-min

As useful as they are, [volcano plots](https://en.wikipedia.org/wiki/Volcano_plot_(statistics)) often take **huge** data input, which means plotting them in HTML will result in generating thousands (or probably millions) of HTML elements for the data points (which is usually an overkill for your browser).

This was an attempt to *work around* this problem. We initially generate the scatter plot using python's [matplotlib](http://matplotlib.org/), define boundaries for a (rectangular) container, get the coordinates of points outside this rectangle and generate a JSON data, which is then loaded into HTML and the `div` elements (points) are distributed relative to the image. Hovering over those elements shows a tooltip.

[Working demo](http://wafflespeanut.github.io/volcano-min)

### Usage

- Make sure that you have matplotlib.
- Set the rectangle's boundaries in `volcano.py` (setting a value to `None` extends the corresponding edge to the adjacent edge of the frame).
- Run `python volcano.py` to generate `plot.png` and `gen.js`
- Open `index.html` to see the changes.
