from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

Typefile = input("Which type of file do you need to open? (image or numerical): ")
if Typefile == "numerical":
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

if Typefile == "image":
    fits_file = input("Enter the path of your file (name of file included): ").strip().strip('"')

    fits_path = Path(fits_file)

    try:
        hdul = fits.open(str(fits_path))
        hdul.info()
    except Exception as e:
        print(f"Error opening file: {e}")
        exit()

    image_data = hdul[0].data
    print(image_data.shape)
    

    plt.figure(figsize=(8, 8))
    plt.imshow(image_data, cmap='inferno', origin='lower', vmin=1000, vmax=3000, alpha=0.7)
    plt.colorbar()
    plt.title(input('Name of your image: '))
    plt.show()
