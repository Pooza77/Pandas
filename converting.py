import pandas as pd
file = pd.read_csv('books.csv')
file.to_html('edu.html')