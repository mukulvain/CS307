from pyomo.environ import *
import matplotlib.pyplot as plt

model = ConcreteModel()

model.X1 = Var(within=NonNegativeReals)
model.X2 = Var(within=NonNegativeReals)
model.X3 = Var(within=NonNegativeReals)
model.X4 = Var(within=NonNegativeReals)

model.Y1 = Var(within=NonNegativeReals)
model.Y2 = Var(within=NonNegativeReals)
model.Y3 = Var(within=NonNegativeReals)
model.Y4 = Var(within=NonNegativeReals)

model.C1 = Constraint(expr=model.X1 + model.X3 <= 100)
model.C2 = Constraint(expr=model.Y1 + model.Y2 <= 100)
model.C3 = Constraint(expr=model.X2 + model.X4 <= 120)
model.C4 = Constraint(expr=model.Y3 + model.Y4 <= 120)
model.C5 = Constraint(expr=model.X1 + model.X3 == model.Y1 + model.Y2)
model.C6 = Constraint(expr=model.X2 + model.X4 == model.Y3 + model.Y4)
model.C7 = Constraint(expr=model.Y1 + model.Y3 == 80)
model.C8 = Constraint(expr=model.Y2 + model.Y4 == 60)

model.cost = Var()
model.ghg_emissions = Var()
model.lead_time = Var()
model.C_cost = Constraint(
    expr=model.cost
    == 1500
    + 3 * model.X1
    + 4 * model.X2
    + 3 * model.X3
    + 2 * model.X4
    + 2 * model.Y1
    + 4 * model.Y2
    + 2 * model.Y3
    + 2 * model.Y4
)
model.C_ghg_emissions = Constraint(
    expr=model.ghg_emissions
    == 12 * model.X1
    + 19 * model.X2
    + 18 * model.X3
    + 23 * model.X4
    + 4 * model.Y1
    + 2 * model.Y2
    + 2 * model.Y3
    + 2 * model.Y4
)
model.C_lead_time = Constraint(
    expr=model.lead_time
    == 2 * model.X1
    + 2 * model.X2
    + 2 * model.X3
    + 2 * model.X4
    + 4 * model.Y1
    + model.Y2
    + 4 * model.Y3
    + 4 * model.Y4
)
model.O_cost = Objective(expr=model.cost, sense=minimize)
model.O_ghg_emissions = Objective(expr=model.ghg_emissions, sense=minimize)
model.O_lead_time = Objective(expr=model.lead_time, sense=minimize)


# Step 1
model.O_ghg_emissions.deactivate()
model.O_lead_time.deactivate()
solver = SolverFactory("glpk")
solver.solve(model)

print(
    "X1 = ",
    value(model.X1),
    "\nX2 = ",
    value(model.X2),
    "\nX3 = ",
    value(model.X3),
    "\nX4 = ",
    value(model.X4),
    "\nY1 = ",
    value(model.Y1),
    "\nY2 = ",
    value(model.Y2),
    "\nY3 = ",
    value(model.Y3),
    "\nY4 = ",
    value(model.Y4),
)
print("Cost = " + str(value(model.cost)))
print("GHG Emissions = " + str(value(model.ghg_emissions)))
print("Total Lead Time = " + str(value(model.lead_time)))
cost_min = value(model.cost)
ghg_emissions_e_1 = value(model.ghg_emissions)

model.O_ghg_emissions.activate()
model.O_cost.deactivate()
solver.solve(model)

print(
    "X1 = ",
    value(model.X1),
    "\nX2 = ",
    value(model.X2),
    "\nX3 = ",
    value(model.X3),
    "\nX4 = ",
    value(model.X4),
    "\nY1 = ",
    value(model.Y1),
    "\nY2 = ",
    value(model.Y2),
    "\nY3 = ",
    value(model.Y3),
    "\nY4 = ",
    value(model.Y4),
)
print("Cost = " + str(value(model.cost)))
print("GHG Emissions = " + str(value(model.ghg_emissions)))
print("Total Lead Time = " + str(value(model.lead_time)))
ghg_emissions_min = value(model.ghg_emissions)

model.O_ghg_emissions.deactivate()
model.O_lead_time.activate()
solver.solve(model)


print(
    "X1 = ",
    value(model.X1),
    "\nX2 = ",
    value(model.X2),
    "\nX3 = ",
    value(model.X3),
    "\nX4 = ",
    value(model.X4),
    "\nY1 = ",
    value(model.Y1),
    "\nY2 = ",
    value(model.Y2),
    "\nY3 = ",
    value(model.Y3),
    "\nY4 = ",
    value(model.Y4),
)
print("Cost = " + str(value(model.cost)))
print("GHG Emissions = " + str(value(model.ghg_emissions)))
print("Total Lead Time = " + str(value(model.lead_time)))
lead_time_min = value(model.lead_time)
ghg_emissions_e_3 = value(model.ghg_emissions)


cost = []
ghg_emissions = []
lead_time = []


e_2_lower_bound = ghg_emissions_min
e_2_upper_bound = max(ghg_emissions_e_1, ghg_emissions_e_3)

# Step 2
n = 100
step_n = (e_2_upper_bound - e_2_lower_bound) // n

# Step 3
e_2 = e_2_upper_bound

while e_2 > e_2_lower_bound:

    # Step 4.1
    model.c2 = Constraint(expr=model.ghg_emissions <= e_2)
    solver.solve(model)
    e_3_lower_bound = value(model.lead_time)

    model.O_cost.activate()
    model.O_lead_time.deactivate()
    solver.solve(model)
    e_3_upper_bound = value(model.lead_time)

    # Step 4.2
    m = 100
    step_m = (e_3_upper_bound - e_3_lower_bound) // m

    # Step 4.3
    e_3 = e_3_upper_bound

    # Step 4.4
    while e_3 > e_3_lower_bound:
        model.c3 = Constraint(expr=model.lead_time <= e_3)
        solver.solve(model)

        # Optain Pareto Optimal
        cost.append(value(model.cost))
        ghg_emissions.append(value(model.ghg_emissions))
        lead_time.append(value(model.lead_time))

        # Step 4.5
        model.del_component(model.c3)
        e_3 -= step_m

    model.del_component(model.c2)
    e_2 -= step_n


fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(10)
ax = plt.axes(projection="3d")
ax.scatter(
    cost, ghg_emissions, lead_time, "o-", c="b", label="Pareto optimal front"
)
ax.set_title("Pareto Optimal Front")
ax.legend(loc="best")
ax.set_xlabel("Cost")
ax.set_ylabel("GHG Emissions")
ax.set_zlabel("Lead Time")
ax.grid(True)
fig.tight_layout()
plt.show()
