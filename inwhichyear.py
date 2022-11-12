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
df_year_publ = var4[["year", "name", "journal", "publisher"]]
agg_func_max_min = {'name':['max', 'min'],
                    'year' :['max', 'min'],
                    'journal':['max', 'min'],
                    'publisher':['max', 'min']}
sorting = df_year_publ.groupby(["year","journal", "publisher"]).agg({
    "name":"count"}).reset_index().agg(agg_func_max_min)
print(sorting)











