
import numpy as np
import pandas as pd
import time
import tskit

import matplotlib.pyplot as plt

def benchmark_GRM(ts):
    before = time.perf_counter()
    D = ts.divergence_matrix(mode="branch")
    duration = time.perf_counter() - before
    data = {"D_time": duration}

    before = time.perf_counter()
    B = ts.genetic_relatedness_matrix(mode="branch")
    duration = time.perf_counter() - before
    data["B_time"] = duration
    return data

def benchmark_GRM_vec(ts):
    before = time.perf_counter()
    w = np.ones(ts.num_samples)
    x = ts.genetic_relatedness_vector(w, mode="branch")
    duration = time.perf_counter() - before
    return {"matvec": duration}


def run_benchmark():

    data = []
    for k in range(1, 7):
        path = f"tmp/chr21_10_{k}.ts"
        ts = tskit.load(path)
        # datum = benchmark(ts)
        datum = benchmark_GRM_vec(ts)
        datum["n"] = ts.num_samples
        data.append(datum)
        df = pd.DataFrame(data)
        print(df)
        df.to_csv("matvec_timing.csv")

def plot():
    df = pd.read_csv("matvec_timing.csv")
    print(df)

    plt.loglog(df.n / 2, df.matvec, marker=".")
    plt.xlabel("Sample size (diploid)")
    plt.ylabel("Execution time (seconds)")
    plt.savefig("matvec-benchmark.pdf")

if __name__ == "__main__":
    # run_benchmark()
    plot()
