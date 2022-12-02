# Supply Chain Management Optimisation

## Multi Objective Optimization using E-constraints method

### Prerequisites
To run the following code, you need to use the following packages.
1. Python 3
1. Matplotlib and Pyplot
1. Pyomo Package
1. GLPK package

Run the following commands in your terminal to execute the file.
1. `sudo apt-get install glpk-utils`
2. `pip install -r requirements.txt`
3. `python multi-opt.py`

### About the Code
Let us assume that there is just chemical reaction happening in the production plants i.e. 
X -> Y.
There are two suppliers, two consumers and two production plants, with the following network.

First, we create X1, X2, X3 and X4 as the non-negative variables for amount of chemical X supplied from raw material supplier to production plants.
Next, we create Y1, Y2, Y3 and Y4