

from setuptools import setup, find_packages



setup(name = "Syx",
version = '0.1.0',
python_requires = '>=3',
install_requires = ['cmd2>=0.8.2', 'gim>=0.1.0', 'upacc>=0.1.0', 'bwamu>=0.1.0'],
description = 'A text based roleplaying/adventure game',
url = 'https://www.github.com/morph8hprom/Syx',
author = 'Devon Blackburn',
author_email = 'morph8hprom@gmail.com',
license = 'GPL 3.0',
packages = find_packages('src'), package_dir = {'' : 'src'},
include_package_data = True,
package_data = {
'' : ['*.txt'],
'' : ['*.json'],
}
)
