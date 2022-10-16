import pandas as pd
df = pd.read_csv('books.csv')
filte = df.loc[(df['Publisher']=='Penguin') & (df['Genre']=='data_science')]
print(filte)
