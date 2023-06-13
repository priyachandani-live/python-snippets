"""
Understanding Decorators
"""

#Assigning a function to a variable
def add(a,b):
    """
    This function adds two values namely a and b
    """
    return a+b

# sum = add(2,3)
# print(sum)

# sum = add
# print(sum)
# print(sum(4,4))
# print(type(add))
# print(add.__doc__)


#calling a function within a function

# def tall(x):
#     return x.upper()

# def short(x):
#     return x.lower()

# def trial(a):
#     # output = a("gorgeous")
#     # output = a
#     return a("happy")

# print(trial(tall))
# print("Trial", trial("abc"))


# print(tall("priya"))




# def create_adder(x):
#     print(x)
#     def adder(y):
#         print(y)
#         return x+y
 
#     return adder
 
# add_15 = create_adder(15)
 
# print(add_15(10))

# def playing_with_function():
#   return "Amazing concept"

# trial = playing_with_function()

# print(trial())


def div(a,b):
    print(a/b)

#I have to modify div function, without actually modifying it
def smart_div(func):
    def inner(a,b):
        """
        trying to make a function like div, but not exactly like div, 
        in other words a function that will do the modification work which could have been possible within the actual div()
        """
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

    # print(func)
    # return func

priya = smart_div(div)
priya(2,4)
