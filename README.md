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
![SC-Network.png](https://github.com/mukulvain/CS307/blob/master/SC%20Network.png)
First, we create X1, X2, X3 and X4 as the non-negative variables for amount of chemical X supplied from raw material supplier to production plants.
Next, we create Y1, Y2, Y3 and Y4 as the non-negative variables for the amount of chemical Y supplied from production plants to the customers.

Then, we add the equality and inequality constraints as a result of mass balances and capacity constraints.
We define 3 variables, i.e.

1. The total Cost
1. GHG emissions
1. Total lead time

and assign them the appropriate values. These are the objective functions which needs to be minimised.

We minimise each objective function independently usnig GLPK package and note the values for GHG emissions in each case, this gives us the lower bound and upper bound on e2.

We then discretise the intervals between the lower bound and upper bound to further get bounds for e3.

We iterate for pair of values i.e. e2 and e3 and obtain a Pareto Optimal Front which is then showcased using Matplotlib-Pyplot package from Python.

This optimisation is made possible using Pyomo, an open source python package for Optimisation.

### Acknowledgement
We thank Prof. Kapil Ahuja for helping us understand the fundamental optimisation concepts. We also thank him for his guidance which helped fuel enthusiasm in working with the problem.

### References
1. Zhang, Q., Shah, N., Wassick, J., Helling, R., & van Egerschot, P. (2014). Sustainable supply chain optimisation: An industrial case study. Computers & Industrial Engineering, 74, 68-83. https://doi.org/10.1016/j.cie.2014.05.002
1. Supply chain management. (2022, October 28). In Wikipedia. https://en.wikipedia.org/wiki/Supply_chain_management
1. Multi-objective optimization. (2022, November 25). In Wikipedia. https://en.wikipedia.org/wiki/Multi-objective_optimization


### Team Members
1. Mukul Jain (200001050)
1. Nilay Ganvit (200001053)