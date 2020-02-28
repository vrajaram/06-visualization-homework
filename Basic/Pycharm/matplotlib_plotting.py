#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os

# Import the file
df = pd.read_csv('data/insurance.csv', header=0)

insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv',
                      sep=',',
                      header=0)

os.makedirs('plots', exist_ok=True)

# Re-do the previous items, adding the title, x label and y label for each item.
# Plot the chart for charges and save it as charges_plot.png (line Plot)
plt.plot(insurance['charges'], color='red')
plt.title('charges')
plt.ylabel('charges')
plt.savefig(f'plots/charges.png', format='png')
plt.clf()

# Plot the histogram for bmi and save it as bmi_hist.png (histogram)
plt.hist(insurance['bmi'], bins=5, color='g')
plt.title('BMI')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plot the scatterplot for age vs charges and save it as age_charge_scatter.png (scatter plot)
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age vs Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_charge_scatter.png', format='png')

# Do the plots match what we saw with the correlation function?
# Not exactly the same but somewhat
print(df[['charges', 'age', 'bmi', 'children']].corr())

plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age vs Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

plt.scatter(insurance['bmi'], insurance['charges'], color='b')
plt.title('bmi vs Charges')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

plt.scatter(insurance['children'], insurance['charges'], color='b')
plt.title('Children vs Charges')
plt.xlabel('Children')
plt.ylabel('Charges')
plt.show()

plt.close()
