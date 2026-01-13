# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
def calculadora():
    print("\n=== CALCULADORA ===")
    print("Operações disponíveis: +, -, *, /")
    
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == '+':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif operacao == '-':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif operacao == '*':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida!")
    else:
        print("Operação inválida!")


# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.
def registro_notas():
    print("\n=== REGISTRO DE NOTAS ===")
    notas = []
    
    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para calcular a média): ")
        
        if entrada.lower() == 'fim':
            break
            
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada!")
            else:
                print("Nota deve estar entre 0 e 10!")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nTotal de alunos: {len(notas)}")
        print(f"Notas registradas: {notas}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada!")


# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.
def verificar_senha():
    print("\n=== VERIFICADOR DE SENHA ===")
    print("Critérios de segurança:")
    print("- Mínimo de 8 caracteres")
    print("- Pelo menos um número")
    
    senha = input("\nDigite sua senha: ")
    
    tem_8_caracteres = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    
    print("\n--- Análise da senha ---")
    print(f"Possui pelo menos 8 caracteres: {'✓ Sim' if tem_8_caracteres else '✗ Não'}")
    print(f"Possui pelo menos um número: {'✓ Sim' if tem_numero else '✗ Não'}")
    
    if tem_8_caracteres and tem_numero:
        print("\n✓ Senha SEGURA! Atende a todos os critérios.")
    else:
        print("\n✗ Senha INSEGURA! Não atende aos critérios de segurança.")


# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
def analisar_numeros():
    print("\n=== ANALISADOR DE NÚMEROS ===")
    pares = []
    impares = []
    
    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
            
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                pares.append(numero)
                print(f"{numero} é PAR")
            else:
                impares.append(numero)
                print(f"{numero} é ÍMPAR")
        except ValueError:
            print("Por favor, digite um número inteiro válido!")
    
    print("\n--- Resumo ---")
    print(f"Números pares: {len(pares)} -> {pares}")
    print(f"Números ímpares: {len(impares)} -> {impares}")
    print(f"Total de números analisados: {len(pares) + len(impares)}")


# Menu principal
if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("             MENU PRINCIPAL")
        print("="*40)
        print("1 - Calculadora")
        print("2 - Registro de Notas")
        print("3 - Verificador de Senha")
        print("4 - Analisador de Números")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            calculadora()
        elif opcao == '2':
            registro_notas()
        elif opcao == '3':
            verificar_senha()
        elif opcao == '4':
            analisar_numeros()
        elif opcao == '0':
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")