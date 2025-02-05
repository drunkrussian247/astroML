from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

fits_file = input("Enter the path of your file (name of file included): ").strip().strip('"')

fits_path = Path(fits_file)

try:
    hdul = fits.open(str(fits_path))
    hdul.info()
except Exception as e:
    print(f"Error opening file: {e}")
    exit()

data = hdul[1].data
print(data.columns)

column_name = input('Which column do you want to inspect? (Be aware that some values are in string and therefore cannot be opened with this program): ')
try:
    column_data = data[column_name]
except KeyError:
    print(f"Error: Column '{column_name}' not found.")
    exit()

print(type(column_data))
print(column_data.shape)
print(column_data[:10])

# Filter data
filtered_column_data = column_data[(column_data > -10) & (column_data < 5)]

# Plot histogram
plt.figure(figsize=(8.5, 5))
plt.hist(filtered_column_data, bins=100, color='blue', alpha=0.5, edgecolor='black')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title(input('Enter the title for the graph: '))
plt.grid(True)
plt.show()
