from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import List, Tuple, Optional


def _safe_import_pandas():
	try:
		import pandas as pd
	except ImportError as exc:  # pragma: no cover - mensagem amigavel
		print("Pandas nao encontrado. Instale com 'pip install pandas'.")
		raise SystemExit(1) from exc
	return pd


def _caminho_ou_default(pergunta: str, nome_default: str) -> Path:
	"""Pega caminho informado ou usa um padrao no diretorio atual."""
	resposta = input(pergunta).strip()
	return Path(resposta) if resposta else Path(nome_default)

# 1 - Crie um programa que le um arquivo CSV de logs de treinamento com a biblioteca pandas,
# calcule e exiba a media e o desvio padrao da coluna tempo_execucao, caso o arquivo nao exista
# ou houver erro na leitura, mostre uma mensagem de erro.

def _garantir_csv_exemplo_logs(caminho: Path) -> None:
	"""Cria CSV de exemplo para logs, se nao existir."""
	if caminho.exists():
		return
	with open(caminho, "w", newline="", encoding="utf-8") as arq:
		escritor = csv.writer(arq)
		escritor.writerow(["run_id", "tempo_execucao"])
		escritor.writerows([
			(1, 1.23),
			(2, 1.35),
			(3, 1.15),
			(4, 1.42),
		])
	print(f"Arquivo de exemplo criado em {caminho}")


def _garantir_csv_pessoas(caminho: Path) -> None:
	"""Cria CSV de pessoas de exemplo se ainda nao existir."""
	if caminho.exists():
		return
	with open(caminho, "w", newline="", encoding="utf-8") as arq:
		escritor = csv.writer(arq)
		escritor.writerow(["nome", "idade", "cidade"])
		escritor.writerows([
			("Ana", 28, "Sao Paulo"),
			("Bruno", 34, "Rio de Janeiro"),
			("Clara", 25, "Belo Horizonte"),
		])
	print(f"Arquivo de exemplo criado em {caminho}")


def _obter_stats_tempo_execucao(caminho: str) -> Optional[Tuple[float, float]]:
	"""Retorna media e desvio de tempo_execucao ou None em caso de erro."""
	pd = _safe_import_pandas()
	try:
		df = pd.read_csv(caminho)
		if "tempo_execucao" not in df.columns:
			print("Coluna 'tempo_execucao' nao encontrada no CSV.")
			return None
		media = df["tempo_execucao"].mean()
		desvio = df["tempo_execucao"].std()
		return media, desvio
	except FileNotFoundError:
		print("Arquivo nao encontrado.")
		return None
	except Exception as exc:
		print(f"Falha ao ler o CSV: {exc}")
		return None

def calcular_media_desvio_csv() -> None:
	caminho = _caminho_ou_default("Caminho do CSV de logs (ENTER para exemplo): ", "exemplo_logs.csv")
	_garantir_csv_exemplo_logs(caminho)
	resultado = _obter_stats_tempo_execucao(str(caminho))
	if resultado is None:
		return
	media, desvio = resultado
	print(f"Media: {media:.4f}")
	print(f"Desvio padrao: {desvio:.4f}")

# 2 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que
# este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuario,
# caso ocorra um erro ao salvar, mostre uma mensagem de falha.

def criar_csv_pessoas() -> None:
	pessoas: List[Tuple[str, int, str]] = [
		("Ana", 28, "Sao Paulo"),
		("Bruno", 34, "Rio de Janeiro"),
		("Clara", 25, "Belo Horizonte"),
	]
	destino = _caminho_ou_default("Salvar CSV em (ENTER para exemplo_pessoas.csv): ", "exemplo_pessoas.csv")
	try:
		with open(destino, "w", newline="", encoding="utf-8") as arquivo:
			escritor = csv.writer(arquivo)
			escritor.writerow(["nome", "idade", "cidade"])
			escritor.writerows(pessoas)
		print(f"Arquivo salvo em {destino}.")
	except Exception as exc:
		print(f"Falha ao salvar o CSV: {exc}")
		return

	consultar = input("Deseja consultar tempo_execucao de um CSV de logs? (s/n): ").strip().lower()
	if consultar == "s":
		caminho_logs = _caminho_ou_default("Caminho do CSV de logs (ENTER para exemplo): ", "exemplo_logs.csv")
		_garantir_csv_exemplo_logs(caminho_logs)
		resultado = _obter_stats_tempo_execucao(str(caminho_logs))
		if resultado is not None:
			media, desvio = resultado
			print(f"Media: {media:.4f}")
			print(f"Desvio padrao: {desvio:.4f}")


# 3 - Crie um programa que leia um arquivo CSV informado pelo usuario, percorrendo cada linha do
# arquivo e a exibe na tela, caso o arquivo nao seja encontrado, mostre uma mensagem de erro.

def ler_csv_linha_a_linha() -> None:
	caminho = _caminho_ou_default("Caminho do CSV para leitura (ENTER para exemplo_pessoas.csv): ", "exemplo_pessoas.csv")
	_garantir_csv_pessoas(caminho)
	try:
		with open(caminho, newline="", encoding="utf-8") as arquivo:
			leitor = csv.reader(arquivo)
			for linha in leitor:
				print(", ".join(linha))
	except FileNotFoundError:
		print("Arquivo nao encontrado.")
	except Exception as exc:
		print(f"Erro ao ler o CSV: {exc}")

# 4 - Crie um programa que leia e escreva arquivos no formato JSON, que salve em um dicionario
# com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados,
# caso o arquivo nao existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.

def escrever_e_ler_json() -> None:
	dados = {"nome": "Joao", "idade": 30, "cidade": "Curitiba"}
	caminho = _caminho_ou_default("Salvar JSON em (ENTER para exemplo_dados.json): ", "exemplo_dados.json")
	try:
		with open(caminho, "w", encoding="utf-8") as arquivo:
			json.dump(dados, arquivo, indent=2, ensure_ascii=True)
		print(f"JSON salvo em {caminho}.")
	except Exception as exc:
		print(f"Falha ao salvar o JSON: {exc}")
		return

	try:
		with open(caminho, encoding="utf-8") as arquivo:
			carregado = json.load(arquivo)
		print("Conteudo lido:")
		print(carregado)
	except FileNotFoundError:
		print("Arquivo JSON nao encontrado para leitura.")
	except Exception as exc:
		print(f"Falha ao ler o JSON: {exc}")


def menu() -> None:
	opcoes = {
		"1": calcular_media_desvio_csv,
		"2": criar_csv_pessoas,
		"3": ler_csv_linha_a_linha,
		"4": escrever_e_ler_json,
	}
	while True:
		print("\nEscolha uma opcao:")
		print("1 - Criar CSV com pessoas")
		print("2 - Media e desvio de tempo_execucao (pandas)")
		print("3 - Ler CSV linha a linha")
		print("4 - Escrever e ler JSON")
		print("q - Sair")
		escolha = input("Opcao: ").strip().lower()
		if escolha == "q":
			print("Encerrando...")
			break
		acao = opcoes.get(escolha)
		if acao:
			acao()
		else:
			print("Opcao invalida.")


if __name__ == "__main__":
	menu()