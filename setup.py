from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='multidst',
    version='0.1.5',
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        'numpy', 
        'pandas',
        'scipy',
        'statsmodels',
        'matplotlib'
    ],
    extras_require = {
        "dev":["twine>4.0.2"],
    },
    python_requires=">=3.10",
    long_description=long_description,
    long_description_content_type='text/markdown'
)

