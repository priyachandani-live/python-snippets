"""
Understanding Decorators
"""

#Assigning a function to a variable
def add(a,b):
    return a+b

# sum = add(2,3)
# print(sum)

sum = add
print(sum(4,4))