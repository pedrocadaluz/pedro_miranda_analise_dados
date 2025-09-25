import pandas as pd
import requests

'''
Exercício 1: Nível Básico (Filtro e Contagem)
Objetivo: Obter dados de todos os personagens e filtrar para encontrar quantos personagens estão "mortos" ou "desconhecidos".

Faça uma requisição à API para o endpoint de personagens (https://rickandmortyapi.com/api/character).

Extraia a lista de personagens da chave "results".

Crie um DataFrame com esses dados.

Usando o Pandas, filtre o DataFrame para contar quantos personagens têm o status igual a "Dead" ou "unknown".

Imprima a contagem final.
'''

# 1. Faz a requisição à API
api_url = "https://rickandmortyapi.com/api/character"
response = requests.get(api_url)
data = response.json()

# 2. Extrai a lista de personagens
characters = data.get("results")

# 3. Cria o DataFrame
df_characters = pd.DataFrame(characters)

# 4. Filtra e conta os personagens com status 'Dead' ou 'unknown'
status_filtrado = df_characters[df_characters['status'].isin(['Dead', 'unknown'])]
contagem = len(status_filtrado)



'''
Exercício 2: Nível Intermediário (Aninhamento e Limpeza de Dados)
Objetivo: Obter a lista de todos os personagens, extrair a dimensão de origem de cada um e limpar os dados de colunas aninhadas.

Faça a mesma requisição do exercício 1 e crie o DataFrame com todos os personagens.

Observe que a coluna origin e location contêm um dicionário. Crie uma nova coluna chamada origin_dimension que armazena a dimensão de origem de cada personagem.

Se a dimensão não estiver disponível, preencha o valor como "Unknown Dimension".

Remova as colunas origin e location do DataFrame para limpar os dados.

Imprima as primeiras 5 linhas do DataFrame resultante.
'''

'''
Exercício 3: Nível Avançado (Múltiplas Requisições e Mesclagem de Dados)
Objetivo: Obter a lista de todos os episódios e, para cada um, encontrar o nome do primeiro personagem que aparece nele, mesclando dados de diferentes APIs.

Faça uma requisição à API para o endpoint de episódios (https://rickandmortyapi.com/api/episode).

Extraia a lista de episódios da chave "results" e crie um DataFrame.

Observe a coluna characters, que é uma lista de URLs. Para cada episódio, encontre o URL do primeiro personagem que aparece.

Faça uma nova requisição à API usando esse URL para obter os dados do primeiro personagem.

Crie uma nova coluna no seu DataFrame de episódios chamada first_character_name com o nome do primeiro personagem de cada episódio.

Dica: Você pode usar um laço de repetição (for) ou a função .apply() do Pandas para iterar sobre as linhas do seu DataFrame e fazer as requisições para cada episódio. 
'''