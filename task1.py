
import pulp

# Define the problem
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Objective function
prob += x + y, "Total Production"

# Constraints
prob += 2 * x + y <= 100, "Water_Limit"
prob += x <= 50, "Sugar_Limit"
prob += x <= 30, "Lemon_Juice_Limit"
prob += 2 * y <= 40, "Fruit_Puree_Limit"

# Solve the problem
prob.solve()

# Print the results
print(f"Optimal number of Lemonade units: {pulp.value(x)}")
print(f"Optimal number of Fruit Juice units: {pulp.value(y)}")
print(f"Total Production: {pulp.value(prob.objective)}")