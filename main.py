import pickle
import numpy as np
from ortools.linear_solver import pywraplp

'''
matrix structure is
from column 0 .. 15
north0 ... north3
east0 ... east3
south0 ... south3
west0 ... west3
north cost is -lat
east cost is -long
south cost is lat
west cost is long
'''
def getCost(lat,long,j):
    if j < 4:
        return -float(lat)
    elif j < 8:
        return -float(long)
    elif j < 12:
        return float(lat)
    else:
        return float(long)

def costify(lat_long):

    teams = lat_long.keys()
    costs = np.zeros((len(teams),len(teams)))

    for i,team in enumerate(lat_long.keys()):
        lat,long = lat_long[team]
        for j in range(len(teams)):
            costs[i][j] = getCost(lat,long,j)
    return costs

def get_team_names(lat_long):
    team_names = []
    for team in lat_long.keys():
        team_names.append(team)
    return team_names

def solveAssignment(costs,team_names):
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    num_workers = len(costs)
    num_tasks = len(costs[0])

    # x[i, j] is an array of 0-1 variables, which will be 1
    # if worker i is assigned to task j.
    x = {}
    for i in range(num_workers):
        for j in range(num_tasks):
            x[i, j] = solver.IntVar(0, 1, '')

    # Each worker is assigned to at most 1 task.
    for i in range(num_workers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) == 1)

    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f'Total cost = {solver.Objective().Value()}\n')
        for j in range(num_tasks):
            if j==0:
                print('North:')
            elif j == 4:
                print('East:')
            elif j == 8:
                print('South:')
            elif j ==12:
                print('West:')
            for i in range(num_workers):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    name = team_names[i]
                    print('\t'+name)
    else:
        print('No solution found.')

if __name__ == '__main__':
    with open('lat_longAFC.pickle','rb') as file:
        lat_long = pickle.load(file)

    costs = costify(lat_long)
    team_names = get_team_names(lat_long)
    print('AFC solutions:')
    solveAssignment(costs,team_names)
