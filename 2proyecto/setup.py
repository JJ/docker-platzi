from setuptools import setup, find_packages
import distutils.cmd

setup(
    name='hitor',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'flask',
      'hitor',
      'gunicorn',
    ],
    tests_require = [
        'pytest',
    ],
    test_suite = 'tests',
    
)
