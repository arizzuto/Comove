from setuptools import setup,find_packages
setup(name='Comove',
      version='1.1',
      py_modules=['Comove'],
      packages=find_packages() + ['resources'],
      include_package_data=True
      )
