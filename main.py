# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(lwd["year"],lwd["WK_working_paid_p"],color="red")
plt.ylim(0, 95)
# add a title to the plot
plt.title("Women Paid For Their Work")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women who worked in the past 12 months and are paid in their work (%)")

oneCountryBooleanList = lwd["country_name"]== "Turkey"
oneCountryData = lwd.loc[oneCountryBooleanList]
print("Setting: There is a 15.6% pay gap between men and women in Turkey")
print("32.5% of women were doing paid work in 2016")
print("40.7% of educated women were not employed in 2016")

print("\nCharacters: Gulden Turktan aimed to reduce poverty by including women in the workforce")
print("Asli E. Mert suggested how gender inequalities in Turkey's workforce lead to financial disparities.")
print("The International Labour Organization and Turkish Employment Agency started Phase 1 of the effort towards women empowerment through employment in 2013-2018")

print("\n Context:  Women were not encouraged to take part in the paid workforce in the early 2000s. ")
print("More women started being compensated for their work in the 2010s.")
print("With self-isolation and economic distress in 2020, less women may have been committed to paid working positions.")
print("")

print("\n Potential Research Questions: How effective were the government's efforts to empower women in the workforce during the Covid-19 pandemic")

# show the plot
plt.show()



