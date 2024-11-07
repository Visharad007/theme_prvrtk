from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in whitetheme_v13/__init__.py
from forest_theme import __version__ as version

setup(
	name='theme_pravartak',
	version=version,
	description='theme for erpnext',
	author='Visharad',
	author_email='vish@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
