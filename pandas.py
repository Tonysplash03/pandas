from sklearn.impute import SimpleImputer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

y = np.round((10*np.random.rand(2, 3)))
print(y+3)
plt.hist(y)
a = np.array([[1, 2, 3], [1, 2, 4]])

print(a[1, 2])
q = np.random.rand(1000000)
print(np.sum(q))
print(np.arange(11))
for i in range(11):
    print(i)

print(np.random.randint(1, 10, size=(5, 3)))

grade = {'A': 4,
         'B': 3,
         'C': 2,
         'D': 1,
         '10': 'hi'}

percent = {'A': 100,
           'B': 80,
           'C': 60,
           'D': 49,
           '10': 'hello'}
percentpd = pd.Series(percent)
gradepd = pd.Series(grade)
print(grade)
print(gradepd)

D = pd.DataFrame({'grade': gradepd, 'percent': percentpd})
E = pd.DataFrame({'grade': grade, 'percent': percent})
E["scalegrade"] = E['percent']
print(D)
print(E.T)
print(pd.DataFrame([{'a': 1, 'b': 4}, {'b': 5, 'c': 8}]))

df = pd.read_csv
print(np.linspace(1, 10, 100))
