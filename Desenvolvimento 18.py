idade=True
while idade:
  try:
    nome=str(input("Nome completo: "))
    ano=int(input("Ano de nascimento: "))
    idade=2022-ano
    if ano<1922 or ano>2021:
        print("Ano inválido!")
    else:
        print("Olá",nome,"sua idade atual é:",idade,"anos")

  except ValueError:
      print("Não foi digitado um número, tente novamente.")
      