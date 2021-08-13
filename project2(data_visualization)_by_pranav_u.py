# -*- coding: utf-8 -*-
"""Project2(data_visualization) by Pranav U.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DdBtDhvi5PguFb2mOimwJb-fSZCJY1OG
"""

# Commented out IPython magic to ensure Python compatibility.
#Project2 Data Visualization by Pranav U.
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import seaborn as sb

# %matplotlib inline

#read the file and print the DataFrame
flights = pd.read_csv('/content/flights_data.csv')
print(flights.shape)
flights.head()

#BarChart of Source of the flights
sb.countplot(data = flights, x = 'Source')
plt.ylabel('Number of flights', fontsize = 12)
plt.xlabel('Source', fontsize = 12)

#BarChart of source in single color
base_color = sb.color_palette()[0]
sb.countplot(data = flights, x = 'Source', color = base_color)
plt.xticks(rotation = 30)

base_color = sb.color_palette()[1]
gen_order = flights['Source'].value_counts().index
sb.countplot(data = flights, x = 'Source', color = base_color, order = gen_order);

base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color);

#rotating the names on x-axis for better view
base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color)
plt.xticks(rotation = 90);

#rotating the chart on Y-axis
base_color = sb.color_palette()[2]
sb.countplot(data = flights, y = 'Airline', color = base_color);

#to find the null values
flights.isna().sum()

na_counts = flights.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation = 90)
plt.ylabel('Number of missing values', fontsize = 12)

#to print the PieChart of the DataFrame
sorted_counts = flights['Destination']. value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90, counterclock = False);
plt.axis('square')
plt.title('Flight Destination\'s')

#to print the DonutChart
sorted_counts = flights['Destination']. value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90, 
        counterclock = False, wedgeprops = {'width' : 0.5})
plt.axis('square')
plt.title('Flight Destination\'s');

#to print Histogram
plt.hist(data = flights, x = 'Duration(minutes)');

plt.hist(data = flights, x = 'Price', bins = 20);

bins = np.arange(0, flights['Price'].max()+1, 1200)
plt.hist(data = flights, x = 'Price', bins = bins)
plt.show()

sb.distplot(flights['Price']);

sb.distplot(flights['Price'], kde = False);

bins_edges = np.arange(0, flights['Price'].max()+1, 1200)
sb.distplot(flights['Price'], bins = bins_edges, kde = False,
            hist_kws = {'alpha' : 1});