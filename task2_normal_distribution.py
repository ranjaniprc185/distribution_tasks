import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp
penguins = sns.load_dataset("penguins")
data = penguins["body_mass_g"].dropna()
mean_value = np.mean(data)
std_value = np.std(data)
print("Mean:", mean_value)
print("Standard Deviation:", std_value)
plt.figure(figsize=(10,6))
plt.hist(data, bins=15, density=True, alpha=0.6, label="Actual Data")
x = np.linspace(data.min(), data.max(), 100)
normal_pdf = (1 / (std_value * sqrt(2 * pi))) * np.exp(-0.5 * ((x - mean_value) / std_value) ** 2)
plt.plot(x, normal_pdf, label="Normal Distribution", linewidth=2)
plt.title("Normal Distribution Fit for Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Density")
plt.legend()
plt.show()
