import pandas as pd 
df = pd.read_excel("C:/pedro_ibmec/analise_dados/livros_classics.xlsx")
df.shape
df.columns
df.head(5)
df.sample(5)