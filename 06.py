# 1 - Gerador de Senhas Aleatórias
import random
import string

def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha}")

# 2 - Buscar Usuário Fictício (API Random User)
import requests

def buscar_usuario_aleatorio():
    try:
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()
        data = response.json()
        usuario = data['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print(f"\nNome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except requests.exceptions.RequestException:
        print("Falha ao conectar com a API.")

# 3 - Consultar CEP (API ViaCEP)
def consultar_cep():
    cep = input("Digite o CEP (somente números): ")
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        response.raise_for_status()
        data = response.json()
        
        if 'erro' in data:
            print("CEP não encontrado.")
        else:
            print(f"\nLogradouro: {data.get('logradouro', 'N/A')}")
            print(f"Bairro: {data.get('bairro', 'N/A')}")
            print(f"Cidade: {data.get('localidade', 'N/A')}")
            print(f"Estado: {data.get('uf', 'N/A')}")
    except requests.exceptions.RequestException:
        print("Falha na requisição.")

# 4 - Consultar Cotação de Moedas (API AwesomeAPI)
def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()
    try:
        response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
        response.raise_for_status()
        data = response.json()
        
        chave = f"{moeda}BRL"
        if chave in data:
            cotacao = data[chave]
            print(f"\nMoeda: {moeda}/BRL")
            print(f"Valor atual: R$ {cotacao['bid']}")
            print(f"Máxima: R$ {cotacao['high']}")
            print(f"Mínima: R$ {cotacao['low']}")
            print(f"Data/Hora: {cotacao['create_date']}")
        else:
            print("Moeda não encontrada.")
    except requests.exceptions.RequestException:
        print("Erro na requisição.")

# Menu Principal
if __name__ == "__main__":
    while True:
        print("\n=== MENU ===")
        print("1 - Gerar senha aleatória")
        print("2 - Buscar usuário fictício")
        print("3 - Consultar CEP")
        print("4 - Consultar cotação de moeda")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            gerar_senha()
        elif opcao == "2":
            buscar_usuario_aleatorio()
        elif opcao == "3":
            consultar_cep()
        elif opcao == "4":
            consultar_cotacao()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")