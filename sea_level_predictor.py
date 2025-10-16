import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, s=20)

    # Create first line of best fit (using all data from 1880 to 2050)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate years from 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred1 = slope1 * years_extended + intercept1
    
    # Plot first line of best fit
    ax.plot(years_extended, sea_level_pred1, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate years from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred2 = slope2 * years_recent + intercept2
    
    # Plot second line of best fit
    ax.plot(years_recent, sea_level_pred2, 'g', label='Best fit line (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
