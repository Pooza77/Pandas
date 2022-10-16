import pandas as pd
df = pd.read_csv('books.csv')
sort = df.sort_values(by='Title',ascending=False)
print(sort)