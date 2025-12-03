# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path
import re

with open('requirements.txt') as f:
	install_requires = [ln.strip() for ln in f if ln.strip() and not ln.startswith('#')]

# Remove core framework if mistakenly added (bench provides frappe)
for core in ("frappe",):
	if core in install_requires:
		install_requires.remove(core)

# Extract version without importing package (avoids importing frappe during build)
version = "0.0.1"
init_path = Path('whitelabel/__init__.py')
if init_path.exists():
	match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", init_path.read_text())
	if match:
		version = match.group(1)

setup(
	name='whitelabel',
	version=version,
	description='ERPNext Whitelabel',
	author='Bhavesh Maheshwari',
	author_email='maheshwaribhavesh95863@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
