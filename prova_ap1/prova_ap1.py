# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv e ncr_ride_regions.xlsx para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento

import pandas as pd
import requests

# 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
df_bookings = pd.read_csv("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\prova_ap1\\ncr_ride_bookings.csv") #dados da corrida
df_bookings["Booking Status"].unique() #verifica os status
status_filtrado = df_bookings[df_bookings['Booking Status'].isin(['Completed'])]
contagem = len(status_filtrado)
print (f"O número de corridas completadas é igual a {contagem}")


# 2 - Qual a proporção em relação ao total de corridas?
df_bookings = pd.read_csv("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\prova_ap1\\ncr_ride_bookings.csv") #dados da corrida
status_filtrado = df_bookings[df_bookings['Booking Status'].isin(['Completed'])]
total_corridas = df_bookings["Date"]


# 3 - Calcule a média e mediana da Distância percorrida por cada Tipo de veículo.
###média da distância das corridas 
df_bookings['Ride Distance'] = df_bookings['Ride Distance'].fillna(0) #preenche com valores 0
df_bookings['Ride Distance'] = df_bookings['Ride Distance'].dropna() #exclui todos os valores NA
media_distancia = df_bookings["Ride Distance"].mean()
print (f"a média das distâncias é {media_distancia } ")

### mediana
df_bookings['Ride Distance'] = df_bookings['Ride Distance'].fillna(0) #preenche com valores 0
df_bookings['Ride Distance'] = df_bookings['Ride Distance'].dropna() #exclui todos os valores NA
mediana_distancia = df_bookings["Ride Distance"].median()
print (f"a mediana das distâncias é {mediana_distancia } ")


# 4 - Qual o Metodo de Pagamento mais utilizado pelas bicicletas ("Bike") ?


# 5 - Faca um merge com ncr_ride_regions.xlsx pela coluna ("Pickup Location") para pegar as regioes das corrifas.
# e verifique qual a Regiao com o maior Valor da corrida?
df_regioes = pd.read_excel("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\prova_ap1\\ncr_ride_regioes.xlsx")
df_bookings = pd.read_csv("C:\\pedro_ibmec\\quarto_semestre\\analise_dados\\prova_ap1\\ncr_ride_bookings.csv") 

## df é left, df_marcas_info é right, on é a coluna em comum, how é o tipo de merge
merge_booking_regioes = pd.merge(df_bookings, df_regioes, on = "Pickup Location", how="inner")

#região com o maior valor de corrida
booking_value = merge_booking_regioes['Booking Value'].max() #maior valor de corrida
regiao = merge_booking_regioes['Regiao']




# 6 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados"
# e filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“venda”).
# Dica Técnica, filtre atraves das coluna FNTSIGLA: df["FNTSIGLA"].str.contains() 
# e depois SERNOME: df["SERNOME"].str.contains() 
api = "http://www.ipeadata.gov.br/api/odata4/Metadados"
dados = requests.get(api).json()['value']
df = pd.DataFrame(dados)

df_fipe =df[df["FNTSIGLA"].str.contains("Fipe.*", regex=True, case=False)]
df_fipe[df_fipe["SERNOME"].str.contains("venda", regex=True, case=False)]

# Descubra qual é o código da série correspondente.
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# e construa um DataFrame pandas com as datas (DATA) e os valores (VALVALOR).
# Converta a coluna de datas para o formato adequado (pd.to_datetime())

SERCODIGO = 'FIPE12_VENBR12'
api = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
requests.get(api)


SERCODIGO = 'FIPE12_VENBR12'
api = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
dados = requests.get(api).json()
dados = dados['value']
df = pd.DataFrame(dados)
df["VALDATA"] = pd.to_datetime(df["VALDATA"], utc=True, errors="coerce")
df["VALDATA"] = df["VALDATA"].dt.tz_convert("America/Sao_Paulo")
df["DATA"] = df["VALDATA"].dt.date




# 7 -  Monte um gráfico de linha mostrando a evolução das vendas ao longo do tempo.
# Dica: você pode usar a biblioteca matplotlib para gerar o gráfico.
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(df["DATA"], df["VALVALOR"])
plt.title("Venda de veiculos no Brasil")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.grid(True)
plt.show()



# 8 - Crie o grafico do bitcoin (ticker: "btc") atraves da api preco-diversos
# Pegue o periodo compreendido entre 2001 a 2025
# Monte um gráfico de linha mostrando a evolução do preco de fechamento
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3MDAwLCJpYXQiOjE3NTg2MjUwMDAsImp0aSI6ImE1MTcyNDFkMjVmMTQzNjE5NmUwZGQ4MjNmNzQwYzYzIiwidXNlcl9pZCI6IjQyIn0.hkjJt-zo7NI3Q_jn6USXVM5bKpdJ0P4ivwuQYzBIGQw"
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {
'ticker': 'btc',
'data_ini': '2001-01-01',
'data_fim': '2025-09-01'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/preco-diversos', params=params, headers=headers)


dados = requests.get(params).json()
dados = dados['value']
df = pd.DataFrame(dados)
df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"], utc=True, errors="coerce")
df["dataHoraCotacao"] = df["dataHoraCotacao"].dt.tz_convert("America/Sao_Paulo")
df["dataHoraCotacao"] = df["dataHoraCotacao"].dt.date
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot(df["dataHoraCotacao"], df["cotacaoVenda"])
plt.title("Cotação Dolár")
plt.xlabel("Ano-Mês")
plt.ylabel("Cotação")
plt.grid(True)
plt.show()



# 9 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# A autenticação é feita via JWT Token no cabeçalho da requisição.
# Acesse a API no endpoint: https://laboratoriodefinancas.com/api/v1/planilhao
# passando como parâmetro a data (por exemplo, "2025-09-23").
# Construa um DataFrame pandas a partir dos dados recebidos.
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROC (Return on Capital) nessa data.
# Exiba o ticker da empresa, setor e o valor do ROC correspondente.
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3MDAwLCJpYXQiOjE3NTg2MjUwMDAsImp0aSI6ImE1MTcyNDFkMjVmMTQzNjE5NmUwZGQ4MjNmNzQwYzYzIiwidXNlcl9pZCI6IjQyIn0.hkjJt-zo7NI3Q_jn6USXVM5bKpdJ0P4ivwuQYzBIGQw"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {
'data_base': "2025-09-23"
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/planilhao',params=params, headers=headers)
response = response.json()
dados = response["dados"]
df = pd.DataFrame(dados)
df.columns
filtro = (df["setor"] == 'tecnologia')
colunas = ["ticker", "setor", "roc"]
df =df[colunas]
df[filtro].sort_values("roc", ascending=False)


# 10 - A API do Laboratório de Finanças fornece informações de balanços patrimoniais de empresas listadas na B3.
# Acesse o endpoint: https://laboratoriodefinancas.com/api/v1/balanco
# usando a empresa Gerdau ("GGBR4") e o período 2025/2º trimestre (ano_tri = "20252T").
# O retorno da API contém uma chave "balanco", que é uma lista com diversas contas do balanço.
# Localize dentro dessa lista a conta cuja descrição é “Ativo Total” e "Lucro Liquido".
# Calcule o Return on Assets que é dados pela formula: ROA = Lucro Liquido / Ativo Totais

import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3MDAwLCJpYXQiOjE3NTg2MjUwMDAsImp0aSI6ImE1MTcyNDFkMjVmMTQzNjE5NmUwZGQ4MjNmNzQwYzYzIiwidXNlcl9pZCI6IjQyIn0.hkjJt-zo7NI3Q_jn6USXVM5bKpdJ0P4ivwuQYzBIGQw"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'PETR4', 
          'ano_tri': '20231T'
          }
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)
dados = response.json()["dados"][0]
dados = dados["balanco"]
df = pd.DataFrame(dados)
filtro = (df["descrição"] == "Ativo Total") & (df["Lucro Liquido"])
df.loc[filtro]["valor"].iloc[0]


#-------------------------------------------------------------------------------------------------------------------------------
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzYxMjE3MDAwLCJpYXQiOjE3NTg2MjUwMDAsImp0aSI6ImE1MTcyNDFkMjVmMTQzNjE5NmUwZGQ4MjNmNzQwYzYzIiwidXNlcl9pZCI6IjQyIn0.hkjJt-zo7NI3Q_jn6USXVM5bKpdJ0P4ivwuQYzBIGQw"
headers = {'Authorization': 'JWT {}'.format(token)}
params = {'ticker': 'PETR4', 
'ano_tri': '20231T'
}
response = requests.get('https://laboratoriodefinancas.com/api/v1/balanco',params=params, headers=headers)

dados = response.json()["dados"][0]
dados = dados["balanco"]
df = pd.DataFrame(dados)
filtro = (df["descrição"] == "Ativo Total") & (df["conta"] == "1")
df.loc[filtro]["valor"].iloc[0]