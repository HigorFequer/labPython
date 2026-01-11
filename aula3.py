idade = int(input("Digite sua idade: "))

if idade < 18:
  if idade < 12:
    print("Você é uma criança")
  else:
    print("Você é um adolescente")
else:
  if idade < 60:
    print("Você é um adulto")
  else:
    print("Você é um idoso")
    
verificar_resultado = lambda nota:"Aprovado" if nota >= 6 else "Reprovado"

nota = float(input("Digite a nota do aluno: "))
print(verificar_resultado(nota))