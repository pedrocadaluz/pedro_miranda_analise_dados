import pandas as pd 
df = pd.read_excel("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\aula1\\livros_classics.xlsx")
df.shape #formatado do dataset
df.columns #nome das linhas
df.head(5) #seleciona uma quantidade de dados que vc quer ver
df.sample(5) #dados aleatorios