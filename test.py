import numpy as np
"""
Given that : Given a square matrix, calculate the absolute difference between the sums of its diagonals.
11 2 4
4 5 6
10 8 -12
"""
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

#getting the primary diagonal sum
primary_diagonal = []
for i in range(len(arr)):
    primary_diagonal.append(arr[i][i])

print(primary_diagonal)
primary_diagonal_np = np.array(primary_diagonal)
primary_diagonal_sum = primary_diagonal_np.sum()
print(primary_diagonal_sum)

#reversing the array---> to get the secondary diagonal sum
arr1 = arr[::-1]
print(arr1)
secondary_diagonal = []
for i in range(len(arr1)):
    secondary_diagonal.append(arr1[i][i])

print(secondary_diagonal)
secondary_diagonal_np = np.array(secondary_diagonal)
secondary_diagonal_sum = secondary_diagonal_np.sum()
print(secondary_diagonal_sum)


#returning the absoulte difference ---> to achieve the absolute differnce in python
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
