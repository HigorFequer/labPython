import requests

def consultar_cep(cep):
  cep = cep.replace("-","").strip()

  if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido. Digite um CEP com 8 números")
    return
  
  url = f"https://viacep.com.br/ws/{cep}/json/"
  resposta = requests.get(url)
  
  if resposta.status_code != 200:
    print("Erro ao acessar a API via CEP")
    return
  
  dados = resposta.json()
  
  if "Erro" in dados:
    print("CEP não encontrado")
    return
  
  print("\n Endereço encontrado")
  print(f"Logradouro: {dados.get('logradouro')}")
  print(f"Bairro: {dados.get('bairro')}")
  print(f"localidade: {dados.get('localidade')}")
  print(f"Estado: {dados.get('uf')}")
  
cep_usuario = input("Digite o CEP: ")
consultar_cep(cep_usuario)