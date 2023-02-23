#check most tags used in quotes
import pandas as pd
import csv
import re

df = pd.read_csv('quotes.csv',names=['quote','author','tag'])

#print(df.head(5))
#stag_separated = [][]
tags = df['tag']

for x, tag in enumerate(tags):
    #print(tag)
    #tag_separated[x].append(str(tag).split(' '))
    df_tag = tags.str.split(' ')
print(df_tag)    