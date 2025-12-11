import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp
data = pd.read_csv("datasets/customer(poission).csv")
numeric_cols = data.select_dtypes(include=['int64','float64']).columns
calls = data[numeric_cols[0]].dropna()
lambda_mean = calls.mean()
plt.figure(figsize=(10,6))
plt.hist(calls, bins=range(int(calls.min()), int(calls.max())+2), density=True, alpha=0.2, label="Actual Data")

x_vals = np.arange(int(calls.min()), int(calls.max())+1)
poisson_pmf = [(exp(-lambda_mean) * (lambda_mean ** x) / factorial(x)) for x in x_vals]

plt.plot(x_vals, poisson_pmf, marker='o', label="Poisson PMF")

plt.title("Daily Call Distribution with Poisson Overlay")
plt.xlabel("Calls Per Day")
plt.ylabel("Probability")
plt.legend()
plt.show()

print("Lambda (Mean):", lambda_mean)
