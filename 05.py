# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Args:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
    
    Returns:
        float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


def programa_gorjeta():
    print("\n=== CALCULADORA DE GORJETA ===")
    
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (%): "))
        
        gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        total = valor_conta + gorjeta
        
        print(f"\nValor da conta: R$ {valor_conta:.2f}")
        print(f"Gorjeta ({porcentagem_gorjeta}%): R$ {gorjeta:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")


# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não".

def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    Args:
        texto (str): A palavra ou frase a ser verificada
    
    Returns:
        bool: True se for palíndromo, False caso contrário
    """
    import re
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = re.sub(r"[^a-zA-Z0-9]", "", texto).lower()
    
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

def programa_palindromo():
    print("\n=== VERIFICADOR DE PALÍNDROMO ===")
    
    texto = input("Digite uma palavra ou frase: ")
    
    if eh_palindromo(texto):
        print("Sim")
    else:
        print("Não")


# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calcular_desconto(preco_original, porcentagem_desconto):
    """
    Calcula o valor do desconto e o preço final.
    
    Args:
        preco_original (float): O preço original do produto
        porcentagem_desconto (float): A porcentagem de desconto
    
    Returns:
        tuple: (valor_desconto, preco_final)
    """
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - valor_desconto
    
    # Arredonda para 2 casas decimais
    valor_desconto = round(valor_desconto, 2)
    preco_final = round(preco_final, 2)
    
    return valor_desconto, preco_final


def programa_desconto():
    print("\n=== CALCULADORA DE DESCONTO ===")
    
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))
        
        valor_desconto, preco_final = calcular_desconto(preco_original, porcentagem_desconto)
        
        print(f"\nPreço original: R$ {preco_original:.2f}")
        print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        print(f"Você economizou: R$ {valor_desconto:.2f}")
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")


# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

def calcular_dias_vida(data_nascimento):
    """
    Calcula quantos dias uma pessoa está viva.
    
    Args:
        data_nascimento (str): Data de nascimento no formato DD/MM/AAAA
    
    Returns:
        int: Número de dias vivos
    """
    from datetime import datetime
    
    # Converte a string para objeto datetime
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.now()
    
    # Calcula a diferença em dias
    diferenca = hoje - nascimento
    return diferenca.days


def programa_dias_vida():
    print("\n=== CALCULADORA DE DIAS DE VIDA ===")
    
    try:
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        
        dias = calcular_dias_vida(data_nascimento)
        anos = dias // 365
        meses = (dias % 365) // 30
        
        print(f"\nVocê está vivo há {dias} dias!")
        print(f"Isso equivale a aproximadamente {anos} anos e {meses} meses.")
        
        # Informações adicionais
        horas = dias * 24
        minutos = horas * 60
        print(f"\nOu ainda:")
        print(f"- {horas:,} horas")
        print(f"- {minutos:,} minutos")
        
    except ValueError:
        print("Erro: Digite uma data válida no formato DD/MM/AAAA!")
    except Exception as e:
        print(f"Erro: {e}")


# Menu principal
if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("MENU PRINCIPAL")
        print("="*40)
        print("1 - Calculadora de Gorjeta")
        print("2 - Verificador de Palíndromo")
        print("3 - Calculadora de Desconto")
        print("4 - Calculadora de Dias de Vida")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            programa_gorjeta()
        elif opcao == "2":
            programa_palindromo()
        elif opcao == "3":
            programa_desconto()
        elif opcao == "4":
            programa_dias_vida()
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
