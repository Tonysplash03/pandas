import json
import pandas as pd
import numpy as np
a = np.array([0, 1])
b = np.array([1, 0])
print(np.dot(a, b))
C = np.array([[1, 1], [2, 2], [3, 3]])
print(C.T)
song = pd.DataFrame({'age': {"ton": 17, 'Hamza': 18}, 'country': {
                    'ton': 'Thailand', 'Hamza': "Somalia"}})
print(song)

Dic1 = {}
Dic2 = {}
with open("info.txt", "r")as f:
    try:
        Dic1 = json.loads(f.read())
        Dic2 = json.loads(f.read())
    except:
        pass
######################################################################
# csv import data from excel
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
print(df.head())  # print the table
# double bracket to bring out Album and soundtrack list
print(df[['Album', 'Soundtrack']])
print(df.loc[0:2, 'Album':"Soundtrack"])  # loc for bring out name for column
# iloc for bring out number * matter with ':'(need to minus one, but loc don't need to)
print(df.iloc[0:3, 1:5])

# change the index
new_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
df_new = df  # df_new is new variable
df_new.index = new_index   # Replacing 0:8 with a:h
print(df.head)


######################################################################

def insert():
    name = input("name")
    age = int(input("age"))
    country = (input("country"))
    Dic1[name] = age
    Dic2[name] = country


for i in Dic1:
    print(i, Dic1[i], "hello")
insert()
x = pd.DataFrame({'Age': Dic1, 'Country': Dic2})
print(x)

with open("info.txt", "w")as f:
    i = json.dumps(Dic1)
    r = json.dumps(Dic2)
    f.write(r)
    f.write(i)
a = {'a': 1, 'b': 2, 'c': 3}
b = {'a': 10, 'b': 20, 'c': 30}
y = pd.DataFrame({'single': a, 'double': b})
y['triple'] = y['double']*10
y['quatriple'] = (np.array([1, 2, 3]))*10
print(y)
