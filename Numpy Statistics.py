import numpy as np
data = list(map(int, input("Enter numbers separated by space: ").split()))
arr = np.array(data)

print("\n----- Statistics Report -----")
print("Mean =", np.mean(arr))
print("Median =", np.median(arr))
print("Standard Deviation =", np.std(arr))
print("Minimum =", np.min(arr))
print("Maximum =", np.max(arr))