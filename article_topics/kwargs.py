"""
Understanding : **kwargs
"""
def test(**kwargs):
    for key, value in kwargs.items():
        print("Key: ", key)
        print("Value: ", value)
        print("--------------------------")

test(a=1, b=3, c=5) #Now passing variable values as key-value pairs