import os
import matplotlib
import matplotlib.pyplot as plt
import ast
import json
import pandas as pd
from collections import OrderedDict

PATH_TO_BENCHMARK = "./benchmark"

data_tests = {}

font = {'family' : 'Ubuntu',
        'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

def generate_data(data):
    os.makedirs(f"./tests/benchmarks", exist_ok=True)
    for test, params in data.items():
        plt.figure(figsize=(10, 7))

        for param, values in params.items():
            ids = list(values.keys())
            vals = list(values.values())
            plt.plot(ids, vals, label=param, linewidth=4)

        plt.title(f'{test} - Cores x Tempo')
        plt.xlabel('Cores(quantidade)')
        plt.ylabel('Tempo(s)')
        plt.xticks([1] + [i for i in range(4, max(ids) + 1, 4)])
        plt.legend()
        plt.grid(True)
        plt.savefig(f"./tests/benchmarks/{test}.png")
        plt.close()

def generate_speedup(data):
    os.makedirs(f"./tests/speedup", exist_ok=True)
    for test, params in data.items():
        plt.figure(figsize=(10, 7))
        for param, values in params.items():
            ids = list(values.keys())[1:]
            current_vals = list(values.values())
            speedup_vals = [] 
            for i in range(1, len(current_vals)):
                speedup = current_vals[i-1] / current_vals[i] if current_vals[i] != 0 else 0
                speedup_vals.append(speedup)
            
            plt.plot(ids, speedup_vals, label=param, linewidth=4)

        plt.title(f'{test} - Speed-Up')
        plt.xlabel('Cores(quantidade)')
        plt.ylabel('Speed-Up n x n-1')
        plt.legend()
        plt.grid(True)
        plt.xticks([2] + [i for i in range(4, max(ids) + 1, 4)])
        plt.savefig(f"./tests/speedup/{test}.png")
        plt.close()


for categories in os.listdir(PATH_TO_BENCHMARK):
    path_to_cat = os.path.join(PATH_TO_BENCHMARK, categories)
    for tests in os.listdir(path_to_cat):
        path_to_benchmark = os.path.join(path_to_cat, tests)
        for num_core in range(1, 33):
            to_file = os.path.join(path_to_benchmark, str(num_core), "small/sim.info")
            with open(to_file) as f:
                data = ast.literal_eval(f.read().replace("L}", "}"))
                
                if not categories in data_tests:
                    data_tests[categories] = {}
                if not tests in data_tests[categories]:
                    data_tests[categories][tests] = {}

                data_tests[categories][tests][num_core] = data['t_elapsed']
                f.close()

with open("./resultados.json", "+w") as f:
    json.dump(data_tests, f)
    f.close()

generate_data(data_tests)
generate_speedup(data_tests)

data_tests = OrderedDict(data_tests)
cols = ['Teste', 'Parâmetros', 'core n x core n-1', 'Speed-up']
df = pd.DataFrame(columns=cols)
for test, params in data_tests.items():
    for params, data in params.items():
        for id in range(2, 33):
            df = df.merge(pd.DataFrame({'Teste': test,
                            'Parâmetros': params,
                            'core n x core n-1': f"{id} x {id - 1}",
                            'Speed-up': data[id]/data[id - 1]}, index=[id - 2]), how="outer")

df = df.sort_values(['Teste', 'Parâmetros'])

df.to_csv("./speed_up.csv")