import requests
import pandas as pd


base_url = "https://api.portaldatransparencia.gov.br/api-de-dados/orgaos-siafi"
base_url1 = "https://servicodados.ibge.gov.br/api/v3/agregados/1705/variaveis?localidades=N7[3501,3301]"
# base_url = "https://api.portaldatransparencia.gov.br/api-de-dados/viagens"
 
# params = {
#     'dataIdaDe': '01/01/2024',
#     'dataIdaAte': '31/01/2024',
#     'dataRetornoDe': '01/01/2024',
#     'dataRetornoAte': '31/01/2024',
#     'codigoOrgao': '01901',
#     'pagina': '1'
# }
 
params = {
    'pagina': '1'
}
 
headers = {
    'chave-api-dados': cr.api_key
}
 
response = requests.get(base_url, headers=headers, params=params)


# print(response.json())
# get response as pandas dataframe

df = pd.DataFrame(response.json())
print(df)

