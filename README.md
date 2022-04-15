# magnetocaloric 1.0.1
#### Developed by Supratim Das
![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)

Effective approach to determine magnetocaloric performance of any magnetic material using python. From isotherm M(H) curves, using the Maxwell Relation the magnetocaloric performance of a material can be calculated with the help of this module.




## Examples of How To Use

### 1. Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install magnetocaloric package.

```bash
pip install magnetocaloric==1.0.1
```
### 2. Manage Excel Spreadsheet
-  Check the main excel spreadsheet from where the M-H data will be fetched by the program, data must be arranged in this format given below. 

![](https://github.com/supratimdasinfo/Magnetocaloric-Effect/blob/main/Screenshot%20(229).png?raw=True)

-  And add one extra magnetic field (Hmax + ∆H) with null magnetic moment values. This is nothing else than to bring magnetic moment values of the last row under calculation.

![](https://github.com/supratimdasinfo/Magnetocaloric-Effect/blob/main/Screenshot%20(232).png?raw=True)

- Create two new files (file extension xlsx) to hold the results obtained after the calculation and definitely make them closed, other wise XlsxWriter will not get access.

###  3. Execution
Run the code at any python based environment ( IDLE, PyCharm, Spyder etc.). But I recommend you simply execute this program using command prompt or IDLE. Open new file in IDLE, encode the above program and execute.

```python

import magnetocaloric.mcepy as mc

print(mc.mce(a, b))

```
Here, 'a' is the total number of temperature and 'b' is the total number of applied magnetic field.
