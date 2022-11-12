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

data =pd.read_csv('overall.csv', index_col='name')
min_cited= data['year'].min()
data[data['year'] == min_cited]
top_10 = data['year'].nsmallest(10)
data[data['year'].isin(top_10)]
print(top_10)
