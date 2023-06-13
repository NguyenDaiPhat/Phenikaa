
import numpy as np

x= [0.0190818,0.0250974,0.0289862,0.0205572,0.0266889]

median = np.median(x)
mean = np.mean(x)
minimum = np.min(x)
maximum = np.max(x)
std = np.std(x)

print("Mean:", mean)
print("Std:", std)
print("Minimum:", minimum)
print("Maximum:", maximum)
