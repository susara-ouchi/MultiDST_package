Usage Guide
===========

This guide provides examples and common use cases for **MultiDST**. Follow these examples to get started with the package and explore its main features.

Importing the Package
---------------------

Start by importing **MultiDST**:

.. code-block:: python

   import yourpackagename

Basic Usage
-----------

Example 1: Quick Start
~~~~~~~~~~~~~~~~~~~~~~

Below is a simple example showing how to use **MultiDST** to achieve a basic task.

.. code-block:: python

   # Import necessary modules
   from yourpackagename import MainClass

   # Initialize the main class
   obj = MainClass(param1="value1", param2="value2")

   # Call a method to perform an operation
   result = obj.some_method()
   print("Result:", result)

Example 2: Loading Data
~~~~~~~~~~~~~~~~~~~~~~~

Here’s an example of loading data with **MultiDST**. 

.. code-block:: python

   from yourpackagename import DataLoader

   # Load data from a file or URL
   data = DataLoader.load("path/to/data.csv")
   print(data.head())

Advanced Usage
--------------

Example 3: Customizing Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For advanced configurations, **MultiDST** provides flexibility through additional parameters:

.. code-block:: python

   obj = MainClass(param1="custom_value", param3=42, advanced_option=True)
   result = obj.complex_method(option="special")
   print("Customized Result:", result)

Example 4: Using with Other Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**MultiDST** integrates well with other libraries like Pandas or NumPy. Here’s an example using it alongside Pandas for data analysis:

.. code-block:: python

   import pandas as pd
   from yourpackagename import Analyzer

   # Load data into a DataFrame
   df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6]})

   # Analyze data with Analyzer
   analyzer = Analyzer()
   analysis_result = analyzer.analyze(df)
   print("Analysis Result:", analysis_result)

Common Errors and Troubleshooting
---------------------------------

Below are some common errors and solutions:

- **Error**: `ModuleNotFoundError: No module named 'yourpackagename'`
  - **Solution**: Ensure that **MultiDST** is installed (`pip install yourpackagename`) and that your environment is active.

- **Error**: `TypeError: missing required positional argument`
  - **Solution**: Check that you provided all required arguments for the method or function.

Additional Resources
--------------------

For more details on advanced topics, see:
- The [API reference](api/modules.rst)
- The [tutorials section](tutorials.rst)

Feel free to experiment and explore more complex workflows with **MultiDST** to make the most of its capabilities.