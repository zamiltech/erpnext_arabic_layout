from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_arabic_layout/__init__.py
from erpnext_arabic_layout import __version__ as version

setup(
	name="erpnext_arabic_layout",
	version=version,
	description="Arabic Layout",
	author="ZamilTec",
	author_email="hello@zamiltec.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
