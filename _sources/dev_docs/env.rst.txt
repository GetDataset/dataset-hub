.. _dev_env:

*************************************
Set up your development environment
*************************************

Fork the dataset-hub repository
#################################

First, you need to `create an account <https://github.com/join>`_ on GitHub 
(if you do not already have one) and fork the 
`project repository <https://github.com/GetDataset/dataset-hub>`_ by clicking 
on the ‘Fork’ button near the top of the page. This creates a copy of the code under your account on the GitHub user 
account. For more details on how to fork a repository see `this guide <https://help.github.com/articles/fork-a-repo/>`_.

The following steps explain how to set up a local clone of your forked git 
repository and how to locally install dataset-hub according to your operating system.

Set up a local clone of your fork
###################################

Clone your fork of the dataset-hub repo from your GitHub account to your local disk:

.. code-block:: bash

   git clone https://github.com/YOUR_USERNAME/dataset-hub.git

and change into that directory:

.. code-block:: bash

   cd dataset-hub

Set up a environment and install dependencies
###############################################

We recommend using pip and virtual environments to manage your Python dependencies. 
First, create and activate a virtual environment. For example, using venv:

.. code-block:: bash

   python -m venv venv

Activate the virtual environment:

.. code-block:: bash

   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

Then, install the projects and required dependencies:

.. code-block:: bash

   pip install -e . # Install dataset-hub project with dependencies

To check that everything is set up correctly, try to import dataset-hub in a Python file or notebook:

.. code-block:: python

   import dataset_hub