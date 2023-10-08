from .mce_2D_Operations.data_2d_operation import mce
from .mce_3D_Distribution.data_3d_plotting import mce_3d
from .MH_Interpolation.interpol import interpol

__all__ = [
    'interpol',
    'mce',
    'mce_3d'
]
# magnetocaloric package
# Developed by Supratim Das
# First release: November 5, 2021
# Email: supratim0707@gmail.com

# This file can include package-level metadata or comments.
# It's executed when the package is imported.

# Example metadata:

__version__ = '1.6.6'  # Package version
__author__ = 'Supratim Das' # Package author
__email__ = 'supratim0707@gmail.com' #Get in Touch
__description__ = 'Effective Approach To Calculate Magnetocaloric Effect Of Any Magnetic Material Using Python'  # Package description
__license__ = 'MIT'  # License information
__url__ = 'https://pypi.org/project/magnetocaloric/'  # URL to the package's repository
__keywords__ = ['magnetism', 'thermodynamics', 'magnetocaloric']  # Keywords describing the package
