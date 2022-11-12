import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
var4 = pd.read_csv("overall.csv")
var = var4[["name", "authors"]]
var1 = var4[["cited_by_papers", "authors"]]
var0 = csv.reader(var4)
df1 =pd.DataFrame([var0], columns=['name', 'authors','journal', 'year', 'publisher', 'cited_by_papers', 'abstract'])
name = var[["name"]]
authors = var[["authors"]]
journal = df1[["journal"]]
year = df1[["year"]]
publisher = df1[["publisher"]]
cited_by_papers = df1[["cited_by_papers"]]
abstract = df1[["abstract"]]

data =pd.read_csv('overall.csv', index_col='authors')
max_cited= data['cited_by_papers'].max()
data[data['cited_by_papers'] == max_cited]
top_10 = data['cited_by_papers'].nlargest(10)
data[data['cited_by_papers'].isin(top_10)]
print(top_10)




plt.rcParams["figure.figsize"]=[7.50,3.50]
plt.rcParams["figure.autolayout"]= True
x = [1,652, data['cited_by_papers'].max(),  "authors"]
#x_val= [0,10]
#y_val = ["authors"]
plt.axis([1,10, 0, top_10.count()])
plt.plot(x, '*-', color='red', markersize=10)

plt.show()

#df = pd.DataFrame(var, columns=('name', 'authors'))
#df.plot(x="name", y="authors")

#df2 =df1[['name']].max(axis=1)
















#df =pd.DataFrame(np.random.rand(10,2), columns=('name', 'authors'))
#df =pd.DataFrame([])



#values = var['authors'].value_counts().keys().tolist()
#counts = var['authors'].value_counts().tolist()

#print(var['authors'].value_counts())
#print(values)
#print(counts)


#df = pd.DataFrame(var1)
#df2 =df1[['cited_by_papers']].max(axis=1)
#print(df.count())
#print (df2)
#df.plot(x="name", y="authors")
#plt.rcParams["figure.figsize"]=[7.50,3.50]
#plt.rcParams["figure.autolayout"]= True
#x = np.random.rand(20)
#plt.plot(x, '*-', color='red', markersize=10)
# plt.show()

