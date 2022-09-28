nome = input("Nome do(a) aluno(a): ")
n1 = float(input ("Primeira nota: "))
n2 = float(input ("Segunda nota: "))
f = int(input("Número de faltas: "))
m = (n1+n2)/2

if m>=7 and f<=3:
   print("O(A) aluno(a)",nome,"foi APROVADO(A)!")
else:
   print("O(A) aluno(a)",nome,"foi REPROVADO(A)!")
  
