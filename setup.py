from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='magnetocaloric',
  version='1.1.8',
  description='Effective Approach To Calculate Magnetocaloric Effect Of Any Magnetic Material Using Python',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/supratimdasinfo/Magnetocaloric-Effect',  
  author='Supratim Das',
  author_email='supratim0707@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['magnetocaloric', 'mcepy', 'magnetic', 'programming', 'code', 'python','supratim'],
  include_package_data=True, 
  packages=['magnetocaloric'],
  install_requires=['num2words', 'matplotlib','xlrd==1.2.0','openpyxl','tableprint','XlsxWriter','numpy'] 
)