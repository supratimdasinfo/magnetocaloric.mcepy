# magnetocaloric 1.1.9
#### Developed by Supratim Das
![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)

Effective approach to determine magnetocaloric performance of any magnetic material using python programming. From isotherm M(H) curves, using the Maxwell Relation the magnetocaloric performance of a material can be calculated with the help of this module.

## What's New
- Relative cooling power (RCP) can be calculated.
- A method to visualize 'Full Width Of Half Maxima' has been employed.
- Another methods to illustrate Tricritical mean field model, 3D Heisenberg model and 3D Ising model have also been employed.


## Examples of How To Use

### 1. Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install magnetocaloric package.

```bash

 pip install magnetocaloric==1.1.9

```
### 2. Manage Excel Spreadsheet
-  Check the main excel spreadsheet from where the M-H data will be fetched by the program, data must be arranged in this format given below. 

![](https://github.com/supratimdasinfo/Magnetocaloric-Effect/blob/main/Screenshot%20(229).png?raw=True)

-  And add one extra magnetic field (Hmax + del_H) with null magnetic moment values. This is nothing else than to bring magnetic moment values of the last row under calculation.

![](https://github.com/supratimdasinfo/Magnetocaloric-Effect/blob/main/Screenshot%20(232).png?raw=True)

- Create two new files (file extension xlsx) to hold the results obtained after the calculation and definitely make them closed, other wise XlsxWriter will not get access.

###  3. Execution
Run the code at any python based environment ( IDLE, PyCharm, Spyder etc.). But I recommend you simply execute this code using command prompt or IDLE. 

```python

import magnetocaloric.mcepy as mc

print(mc.mce(a, b))

```
Here, 'a' is the total number of temperature and 'b' is the total number of applied magnetic field.

## Caution

- Before adding the Hmax + del_H value into the M(H) spreadsheet, The maximum value of applied magnetic field (Hmax) must be the multiple of (10xdel_H). As an example, if del_H = 500 Oe / 0.05 T, Hmax must be like 5000 Oe/0.5 T, 10000 Oe / 1 T, 15000 Oe / 1.5 T,........ or any other multiple of (10x500 Oe) whether the value of the magnetic field is Tesla or Oersted. For another example, if del_H = 700 Oe / 0.07 T, Hmax must be like 7000 Oe/0.7 T, 14000 Oe / 1.4 T, 21000 Oe / 2.1 T,........ or any other multiple of (10x700 Oe). Otherwise Hmax for not being a proper numbered figure, an error may occur. This caution is also applicable to the previous versions of the package as well.