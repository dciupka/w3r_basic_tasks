"""Write a Python program to get the Python version you are using"""
import sys

print(f'Version:        {sys.version}')
print(f'Verison info:   {sys.version_info}')

# --------------------------------------------------------------------
import platform

print(platform.python_version())
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))
