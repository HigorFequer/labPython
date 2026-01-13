# 1- Classificador de Idade
# 
# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:
# 
# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

def classificar_idade(idade: int) -> str:
	if idade < 0:
		return "Idade inválida"
	if idade <= 12:
		return "Criança"
	if idade <= 17:
		return "Adolescente"
	if idade <= 59:
		return "Adulto"
	return "Idoso"

# 2- Calculadora de IMC
# 
# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
# 
# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
	if altura <= 0:
		raise ValueError("Altura deve ser maior que zero")
	imc = peso / (altura ** 2)
	if imc < 18.5:
		classificacao = "Abaixo do peso"
	elif imc < 25:
		classificacao = "Peso normal"
	elif imc < 30:
		classificacao = "Sobrepeso"
	else:
		classificacao = "Obeso"
	return imc, classificacao

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def converter_temperatura(valor: float, origem: str, destino: str) -> float:
	origem = origem.lower()
	destino = destino.lower()
	if origem == destino:
		return valor

	# Normaliza para Kelvin como etapa intermediária
	if origem == "c":
		kelvin = valor + 273.15
	elif origem == "f":
		kelvin = (valor - 32) * 5 / 9 + 273.15
	elif origem == "k":
		kelvin = valor
	else:
		raise ValueError("Unidade de origem inválida. Use C, F ou K.")

	if destino == "c":
		return kelvin - 273.15
	if destino == "f":
		return (kelvin - 273.15) * 9 / 5 + 32
	if destino == "k":
		return kelvin
	raise ValueError("Unidade de destino inválida. Use C, F ou K.")
 
# 4- Verificador de Ano Bissexto
# 
# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

def eh_bissexto(ano: int) -> bool:
	if ano % 400 == 0:
		return True
	if ano % 100 == 0:
		return False
	return ano % 4 == 0


def main() -> None:
	print("1) Classificador de Idade")
	idade = int(input("Informe sua idade: "))
	print(f"Categoria: {classificar_idade(idade)}")

	print("\n2) Calculadora de IMC")
	peso = float(input("Informe seu peso (kg): "))
	altura = float(input("Informe sua altura (m): "))
	imc, classificacao = calcular_imc(peso, altura)
	print(f"IMC: {imc:.2f} - {classificacao}")

	print("\n3) Conversor de Temperatura")
	valor = float(input("Informe a temperatura: "))
	origem = input("Unidade de origem (C/F/K): ")
	destino = input("Unidade de destino (C/F/K): ")
	convertido = converter_temperatura(valor, origem, destino)
	print(f"Resultado: {convertido:.2f} {destino.upper()}")

	print("\n4) Verificador de Ano Bissexto")
	ano = int(input("Informe o ano: "))
	if eh_bissexto(ano):
		print("É bissexto")
	else:
		print("Não é bissexto")


if __name__ == "__main__":
	main()