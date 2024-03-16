# Magnetocaloric - Python Module for Magnetocaloric Performance Analysis

![Logo](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/mcepylogo.png?raw=True)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?)
[![Downloads](https://static.pepy.tech/badge/magnetocaloric/month)](https://pepy.tech/project/magnetocaloric)
![Repo Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Contributors](https://img.shields.io/github/contributors/supratimdasinfo/magnetocaloric.mcepy)
![Code Size](https://img.shields.io/github/languages/code-size/supratimdasinfo/magnetocaloric.mcepy)
![Closed Issues](https://img.shields.io/github/issues-closed/supratimdasinfo/magnetocaloric.mcepy)
![Last Commit](https://img.shields.io/github/last-commit/supratimdasinfo/magnetocaloric.mcepy)



## Overview

**magnetocaloric** is a powerful Python module designed to determine the magnetocaloric performance of magnetic materials. Developed by Supratim Das, this module provides an effective way to analyze magnetic behavior and parameters using isotherm M(H) curves and the Maxwell Relation.

## Key Features

- Import M-H data from XLSX files.
- Interpolate magnetic moment polynomially or linearly for precise analysis and visualization.
- Generate various insightful graphs, including:

| Graph Description                           | g_name     |
|--------------------------------------------|-------------------|
| M vs H (Magnetization vs Magnetic Field)   | `MH_plot`         |
| M vs T (Magnetization vs Temperature)      | `MT_plot`         |
| Entropy Change vs T                        | `dSmT_plot`       |
| Mean Field Arrott Plot                     | `MFT_plot`        |
| Temperature depedence of N exponent                     | `N_plot`        |
| Modified Arrott's Plot                     | `arrott_plots`     |
| Susceptibility and Inverse Susceptibility vs T | `sus_plot`     |
| Relative Cooling Power                     | `RCP_plot`        |

This table provides a clear and concise overview of the various graphs and their corresponding `g_name` in your Python module.
- Combine and visualize all graphs at once using `all_plots`.
- Save calculated data for future use with the `save_data` option.
- Automatically create an output folder to store results as XLSX files in the source file's directory.
- Visualize 3D models of:

| 3D Model Description                                        | g_name   |
|------------------------------------------------------------|-----------------|
| Magnetization distribution              | `MH_show`       |
| dM/dT distribution                   | `dMdT_show`     |
| dM/dH distribution                 | `dMdH_show`     |
| Entropy change distribution for comprehensive data analysis | `dSm_show` |
| d^2M/(dT.dH) distribution                 | `d2MdTH_show`     |

This table provides a clear and concise overview of the 3D models and their corresponding `g_name`.

- Intuitive Graphical User Interface: Simplifying Program Interaction. Experience seamless interaction with our PyQt5-powered UI. Standalone Python executable created using PyInstaller - no additional dependencies required.

![GUI](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/GUIv3.PNG?raw=True)

For the Python programming approach, follow the steps in the README.

## Installation

You can easily install the **magnetocaloric** package using pip. Open your command-line interface and run the following command:

```shell
pip install magnetocaloric==1.7.1
```

This will install the specified version of the **magnetocaloric** package.


## Examples of How To Use

### 1. Managing Excel Spreadsheet

Before using the **magnetocaloric** module, ensure that your Excel spreadsheet follows this specific format for M-H data:

![Excel Spreadsheet Format](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/format.png?raw=True)

- The first row and column should contain temperature and applied magnetic field values.
- Fill the corresponding cells with numeric float values (do not use any alphabetic characters).
- Optionally, you can add an extra magnetic field value (`Hmax + del_H`) with null magnetic moment values. This helps align the magnetic moment values of the last row for calculation but is not necessary.

### 2. Execution

To utilize the functions in **magnetocaloric**, follow these steps:

one can structure the code in a class called mceanalysis to provide a unified interface for using the functions from the mcepy module :

```python
from magnetocaloric import mcepy as mp

class mceanalysis:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def run_interpolation(self):
        mp.interpol(**self.kwargs)
        
    def plot_mce_data(self):
        mp.mce(**self.kwargs)

    def plot_mce_3d_data(self):
        mp.mce_3d(**self.kwargs)
        
```
To interpolate the Magnetic Moment data within a user-defined range of field values and a specified interval, the `interpol` function is available. This function offers flexibility by allowing users to set arguments such as `interpol_type`, `interpol_mode` and `degree` for interpolation with minimal error. 

```python
interpolator = mceanalysis(
    path='D:\python\interpolation\mce_example.xlsx',
    sheet_index=1,
    T_row=1,
    H_col='A',
    int_val=0,
    final_val=50000,
    interval=500,
    interpol_type='lin',
    interpol_mode='None',
    deg='None'
)

interpolator.run_interpolation()

```

Explanation of the `interpol` function parameters:

- `path`: Specify the path to your Excel spreadsheet containing M-H data.
- `sheet_index`: Set the spreadsheet index within the Excel file.
- `T_row` and `H_col`: Specify the row and column for actual temperature and field values.
- `int_val`: Set the initial value of the applied magnetic field (H).
- `final_val`: Define the maximum applied field value for data interpolation.
- `interval`: Set the interval for interpolation.
- `interpol_type`: Choose the interpolation type. For linear interpolation, use `'lin'`. For polynomial interpolation, use `'poly'`.
- `interpol_mode`: For polynomial interpolation, choose between `'auto'` (automatically finds the best degree) or `'manual'` (set the degree manually using the `deg` argument).
- `deg`: If using manual polynomial interpolation, specify the degree as an integer.

> **Warning**
The interpolated data will overwrite the source file specified in the `path`. Exercise caution when using this function.

#### Example: Polynomial Interpolation with Different Degrees

You can perform polynomial interpolation with different degrees using the **magnetocaloric** module. In this example, we'll interpolate the data with degree 3 and visualize the results. The image provided below demonstrates the square error of the interpolated data when compared to the original provided data. By visualizing this error, users can easily determine the degree at which the interpolation minimizes error while using polynomial interpolation. Lower error values signify a better fit, indicating that the chosen degree provides a closer approximation to the original data. This graphical representation helps users make informed decisions about the appropriate degree for their specific data sets, ultimately ensuring accurate and reliable results.


```python
interpolator = mceanalysis(
    path='D:/python/interpolation/MCE_example.xlsx',
    sheet_index=1,
    T_row=1,
    H_col='A',
    int_val=0,
    final_val=50000,
    interval=500,
    interpol_type='poly',
    interpol_mode='manual',
    deg=3  # To visualize with degree 2, change to deg=2
)

interpolator.run_interpolation()

```

Here, you can compare the interpolation results for different degrees in the following image:

![](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/interpolation.jpg?raw=True)


### Using the `mce` Function for Customizable Graphs

The **magnetocaloric** module provides a versatile `mce` function that allows you to plot various graphs with high customization. Here's how you can use it:

```python
plotter = mceanalysis(
    samp_name="unknown",
    file_dir='D:\python\mce_example.xlsx',
    sheet_index=1,
    T_row=1,
    H_col='A',
    g_name='dSmT_plot',
    M_unit='emu/g',
    H_unit='Oe',
    T_unit='K',
    plot_legend='Yes',
    loc='upper right',
    field='None',
    linear_threshold='None',
    save_data='allow'
)

plotter.plot_mce_data()

```

Explanation of the function parameters:

- `samp_name`: Specify the sample name or identifier.
- `file_dir`: Provide the source data directory (Excel file path).
- `sheet_index`: Set the spreadsheet index within the Excel file.
- `T_row` and `H_col`: Specify the row and column for actual temperature and field values.
- `g_name`: Set the graph identity from the options listed above.
- `M_unit`, `H_unit`, `T_unit`: Define the units for magnetic moment, magnetic field, and temperature, respectively.
- `plot_legend` and `loc`: Decide whether to display legends on the graph and their position.
- `field` and `linear_threshold`: These are specific to susceptibility graph plotting. `field` specifies the field value for plotting susceptibility, and `linear_threshold` (range: -1 to +1) adjusts the linear regression for finding the Curie-Weiss temperature.
- `save_data`: Allow or disallow the saving of calculated data in new files.

> **Note** 
The `field` and `linear_threshold` arguments are used for susceptibility graph plotting. Unless you need to plot susceptibility or all graphs together, you can leave them as 'None'.

#### Example: Susceptibility and Inverse Susceptibility Plotting

In this example, we will plot the susceptibility and inverse susceptibility by specifying the field and adjusting the linear threshold for a precise fit.

```python
plotter = mceanalysis(
    samp_name="unknown",
    file_dir='D:/python/MCE calculation/MCE_example.xlsx',
    sheet_index=1,
    T_row=1,
    H_col='A',
    g_name='sus_plot',
    M_unit='emu/g',
    H_unit='Oe',
    T_unit='K',
    plot_legend='Yes',
    loc='upper right',
    field='1020.40816',
    linear_threshold=0.9995,
    save_data='allow'
)

plotter.plot_mce_data()

```

In this case, we set the `linear_threshold` near unity to achieve the best linear fit in the higher temperature linear inverse susceptibility region (Curie-Weiss region).
![](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/susceptibility.jpg?raw=True)


### Using the `mce_3d` Function for 3D Data Visualization

The **magnetocaloric** module provides a powerful `mce_3d` function for visualizing data distribution in 3D. Here's how you can use it:

```python
plotter_3d = mceanalysis(
    path="D:/python/MCE calculation/MCE_example.xlsx",
    sheet_index=1,
    T_row=1,
    H_col='A',
    g_name='dSm_show',
    M_unit='emu/g',
    H_unit='Oe',
    T_unit='K',
    dpi=1600,
    save_data='allow'
)

plotter_3d.plot_mce_3d_data()

```

Explanation of the function parameters:

- `path`: Specify the path to the Excel file containing the data.
- `sheet_index`: Set the spreadsheet index within the Excel file.
- `T_row` and `H_col`: Specify the row and column for actual temperature and field values.
- `g_name`: Choose the type of 3D data distribution you want to visualize. Options include those provided above.
- `M_unit`, `H_unit`, `T_unit`: Define the units for magnetic moment, magnetic field, and temperature, respectively.
- `sheet_index`: Set the spreadsheet index within the Excel file.
- `T_row` and `H_col`: Specify the row and column for actual temperature and field values.
- `dpi`: Adjust the resolution of the distribution image.
- `save_data`: Allow or disallow the saving of calculated data in new files.

#### Example: Magnetic Moment (M) Distribution in 3D

In this example, we visualize the magnetic moment (M) distribution in 3D. The resulting image allows you to view the distribution from different perspectives.

![](https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/mce_3d.jpg?raw=True)



## Contributing
### We Welcome Your Contributions!

If you're interested in contributing to the development of this project, your contributions are highly appreciated. Whether you find a bug, have an idea for a new feature, or want to improve the code, you can do so by raising an issue or pull request on our GitHub repository. Your input helps make this project better for everyone.

Feel free to explore the code, try out the application, and share your thoughts with us. We value the contributions of our community members and look forward to collaborating with you. Let's make this project even more amazing together!

#### Project Guide: 

- <img src="https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/sudiptapal.png?raw=True" alt="Sudipta Pal" width="25" height="25"> Sudipta Pal

#### Contributors: 

- <img src="https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/bhaskarbiswas.png?raw=True" alt="Bhaskar Biswas" width="25" height="25">  Bhaskar Biswas
- <img src="https://raw.githubusercontent.com/supratimdasinfo/magnetocaloric.mcepy/main/images/dipanjanbiswas.png?raw=True" alt="Dipanjan Biswas" width="25" height="25">  Dipanjan Biswas



### Contact Information: 

If you have any questions or need assistance, you can reach out to me directly via email at supratim0707@gmail.com.


