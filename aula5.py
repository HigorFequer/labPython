# Program para verificar a cotação do dólar em tempo real

import requests

converter_para_real = lambda valor, cotacao: valor * cotacao

def obter_cotacao_dolar():
  try: 
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if "USDBRL" in dados:
      return float(dados["USDBRL"]["bid"])
    else:
      return None
    
  except requests.exceptions.RequestException:
    print("Erro ao tentar acessar a API de cotação")
    return None

def main():
  try:
    valor_dolar = float(input("Digite o valor em Dólar (USD): "))
    
    cotacao = obter_cotacao_dolar()
    
    if cotacao:
      valor_real = converter_para_real(valor_dolar, cotacao)
      print(f"\nUSD {valor_dolar: .2f}")
      print(f"cotação: R$ {cotacao: .2f}")
      print(f"Valor em reais: R$ {valor_real:.2f}")
    else:
      print("Não foi possível obter a cotação")
      
  except ValueError:
    print("Digite um número válido")
  except Exception as erro:
    print("Erro inesperado", erro)
main()