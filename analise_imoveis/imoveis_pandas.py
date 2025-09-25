import pandas as pd 
df = pd.read_csv("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\analise_imoveis\\imoveis_brasil.csv")
df.shape
df.columns
df.head(5)
df.tail(5)
df.sample(5)
df.info()
# Verificar os tipos de imóveis
df["Tipo_Imovel"].unique()
# Imoveis com valor maiores que 1M
filtro = df["Valor_Imovel"] > 1000000
df_1M = df.loc[filtro]
# selecionar cidade, bairro e valor
colunas_selecionadas = df["Cidade", "Bairro", "Valor_Imovel"]
df2 = df[colunas_selecionadas]
#ordenar os valores dos imóveis mais caros 
df.sort_values(["Valor_Imovel"], ascending=True)
#valor medio dos imoveis
valor_medio_geral = df["Valor_Imovel"].mean()
# valor medio dos imoveis de Curitiba 
filtro = df["Cidade"] == "Curitiba"
valor_medio = df.loc[filtro, ["Valor_Imovel"]].mean()
#numero de imvoveis com valor acima do valor medio
filtro = df["Valor_Imovel"] > valor_medio_geral
df_maior = df.loc[filtro]
len(df_maior)
#numero de imoveis abaixo do valor medio 
filtro = df["Valor_Imovel"] > valor_medio_geral
df_menor = df.loc[filtro]
len(df_menor)