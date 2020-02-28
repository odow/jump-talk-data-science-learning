import json
from pulp import *
import sys
import time

def run_diet_model(filename, verbose = True):
    with open(filename, 'r') as io:
        data = json.load(io)

    Ingredients = list(data.keys())

    prob = LpProblem("DietProblem", LpMinimize)

    quantity = LpVariable.dicts("Ingr", Ingredients, 0)

    prob += lpSum([data[i]['cost'] * quantity[i] for i in Ingredients])

    prob += lpSum([quantity[i] for i in Ingredients]) == 100
    prob += lpSum([data[i]['protein'] * quantity[i] for i in Ingredients]) >= 8.0
    prob += lpSum([data[i]['fat'] * quantity[i] for i in Ingredients]) >= 6.0
    prob += lpSum([data[i]['fibre'] * quantity[i] for i in Ingredients]) <= 2.0
    prob += lpSum([data[i]['salt'] * quantity[i] for i in Ingredients]) <= 0.4

    prob.solve()

    print("Status:", LpStatus[prob.status])
    if verbose:
        for v in prob.variables():
            print(v.name, "=", v.varValue)
    print("Total Cost of Ingredients per can = ", value(prob.objective))

if len(sys.argv) >= 2:
    t = time.time()
    run_diet_model(sys.argv[1], verbose = sys.argv[-1] == "--verbose")
    print("Run time (s) = ", time.time() - t)
