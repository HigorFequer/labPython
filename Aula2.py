def saudacao():
  nome = input("Digite o seu nome: ")
  print(f"Olá, {nome}!\nSeja bem vindo(a) ao mundo de tecnologia")

saudacao()


tentativas = 0
max_tentativas = 3


while tentativas < max_tentativas:
  try: 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print("Resultado da divisão", resultado)
    break #Sai do loop se der certo
  
  except ValueError:
    tentativas += 1
    print(f"Erro: digite apenas números. tentativa {tentativas}/3\n")
    
  except ZeroDivisionError:
    tentativas += 1
    print(f"Erro: não é possível dividir por zero. Tentativas {tentativas}/3\n")
    
  finally:
    if tentativas == max_tentativas:
      print("Número máximo de tentativas atingido. Encerrando programa")