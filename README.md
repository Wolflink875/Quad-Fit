# Quad-Fit
Basic overview of Functionality:
Takes data from Data
Takes data from Data2
Displays plot of data for reference
Asks for user to input ranges for quadratic fit. (currently plot 1 is blue and plot 2 is orange)
If any one query is left blank, values will default to a pre-determined range
(This only occurs when 'cancel' is selected. An error occurs when values are left blank and 'ok' is pressed.
I can't be bothered to fix this for the time being)

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
The vertical placement of data2 is increased arbitrarily for easier visualization

In addition, after closing figure 2 (only if quad fit is selected) a new range is used to find the minimum of the select range on plot 2, and then draws lines at those points.
A line is also drawn halfway between the above mentioned points.

There is now a terminal for easier user input of the min range.
Finally, the program locates the intersection point between the min lines and plot 1. This is done for both mins.
