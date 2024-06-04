from setuptools import setup, find_packages

setup(
    name='multidst',
    version='0.0.1',
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
)

