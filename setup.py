from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),  # Crucial: Finds your packages!
    package_dir={"": "src"},  # Important: Tells setuptools where packages are
)