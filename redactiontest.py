#redaction writing test
import pandas as pd
import random
import numpy as np


whole= pd.read_csv('animes.csv') #whole entire anime csv (contains names, rank, reviews, avg score, etc...)
df = whole[['title', 'synopsis', 'popularity']].copy() #grab smaller dataframe with only names, popularity rank, and synopsis
df = df.sort_values('popularity') #sort by popularity since I'm only grabbing the top 500ish
df = df.drop_duplicates(subset=['title']) #had some duplicates with unique ids, so I removed them
df = df.head(500) # take only the first 500 values 

df['synopsis'] = df['synopsis'].astype(str) # tired reading the synopsis as a string type instead of object so I could use .replace()
df['title'] = df['title'].astype(str)
print(df.dtypes) # still gives me the synopsis and title as objects instead of strings and I can't figure out why

originalSynop = df.iloc[0]['synopsis'] #grab the original synopsis
synopTitle = df.iloc[0]['title'] #grab the corresponding title from that synopsis
print()

print(synopTitle)
print(originalSynop)

print()
	
originalSynop = str(originalSynop) #turn this into a string
synopTitle = str(synopTitle) #turn this into a string

newSynop = originalSynop.replace(synopTitle, 'REDACTED') # everytime the title is mentioned in the synopsis, replace it with redacted
df['synopsis'] = df['synopsis'].replace(originalSynop, newSynop)
#df.at[0, 'synopsis'] = newSynop
#df.set_value(0, 'synopsis', newSynop) # set the synopsis at row x to the newSynop

#print(newSynop)
#df['column name'] = df['column name'].replace(['old value'],'new value')

print(df.iloc[0]['title'])
print(df.iloc[0]['synopsis'])