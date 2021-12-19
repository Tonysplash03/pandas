import pandas as pd
x = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(pd.__version__)
print(x.values)
y = [1, 2, 3, 4, 5]
print(y[::-1])
print(1/1)
print(int(False))
print("hello".upper())
x = (5, 106, 5, 2, 1)
print(len(x))

for i, Y in enumerate(y):
    print(i, Y)
print(sorted(x))

L = [1, 3, 2]
sorted(L)
print(L)
