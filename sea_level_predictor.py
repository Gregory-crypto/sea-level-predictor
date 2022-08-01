import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  fig, ax = plt.subplots( figsize = (15, 8))
  plt.style.context('seaborn')

  ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  

    # Create first line of best fit
  res1880 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  ext_years = np.arange(1880, 2051, 1)
  ax.plot(ext_years, res1880.intercept + res1880.slope * ext_years, 'r')
    # Create second line of best fit
  res2000 = linregress(df['Year'][120:], df['CSIRO Adjusted Sea Level'][120:])
  ax.plot(ext_years[120:], res2000.intercept + res2000.slope * ext_years[120:], 'g')
    # Add labels and title
  ax.set_ylabel('Sea Level (inches)')
  ax.set_xlabel('Year')
  ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()