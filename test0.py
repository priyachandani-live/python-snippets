"""
Given: 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.
arr = [1,1,0,-1,-1]
"""
# arr = [1,1,0,-1,-1]
arr = [-4, 3, -9, 0, 4, 1]
def plus_minus(array):
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in array:
        if i < 0:
            count_negative = count_negative + 1
        if i == 0:
            count_zero = count_zero + 1
        if i > 0:
            count_positive = count_positive + 1
    positive_ratio = count_positive/len(array)
    negative_ratio = count_negative/len(array)
    zero_ratio = count_zero/len(array)
    print(f'positive ratio {positive_ratio:.6f}')
    print(f'negative ratio {negative_ratio:.6f}')
    print(f'zero ratio {zero_ratio:.6f}')


plus_minus(arr)