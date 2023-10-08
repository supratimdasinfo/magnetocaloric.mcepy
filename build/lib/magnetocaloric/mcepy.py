# Import necessary libraries
import sys
import matplotlib.pyplot as plt

# Import modules from different packages
from .mce_2D_Operations.data_2d_operation import mce
from .mce_3D_Distribution.data_3d_plotting import mce_3d
from .MH_Interpolation.interpol import interpol

# Suppress warnings if not already suppressed
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

# Customize font size for matplotlib
plt.rcParams.update({'font.size': 7})


