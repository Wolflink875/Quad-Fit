# Quad-Fit
Basic overview of Functionality:
Takes data from Data
Takes data from Data2
Displays plot of data for reference
Asks for user to input ranges for quadratic fit. (currently plot 1 is blue and plot 2 is orange)
If any one query is left blank, values will default to a pre-determined range

It will ask if you wish to invert either plot 1 or 2 or both. This is only necessary when fitting for a maximum.
(currently needs an option to not invert either plot)

Reads the desired range of data points
Cuts data out into own matrix
Imposes this range onto the original (or inverted) plots

If the user confirms, the quadratic fit will also be imposed onto the plot. Note that attempting to do a fit for
a maximum without inverting will result in errors.
Calculates difference between minima

Corrects 'Time' of Data2 by difference between minima
Displays plot with correction

In addition, after closing figure 2 (only if quad fit is selected) a new range is used to find the minimum of a select range on plot 2, and then draw lines at those points and directly between.
More user-based interactivity will be added soon
