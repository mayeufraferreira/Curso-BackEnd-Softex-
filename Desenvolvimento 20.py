import pandas as pd
df = pd.read_csv ("C:/Users/mayka/OneDrive/Documentos/notas_alunos.csv")
media = (df["nota_1"] + df["nota_2"])/2

df["média"] = media

df.loc[df["média"] >=7, "situação"] = "APROVADO"
df.loc[df["média"] <7 | df["faltas"] >5, "situação"] = "REPROVADO"

df.to_csv("C:/Users/mayka/OneDrive/Documentos/alunos_situacao.csv")

maiorNumFaltas = df["faltas"].max()
print("O maior números de faltas é:",(maiorNumFaltas))

mediaGeral = df["média"].mean()
print("A média geral das notas é:",(mediaGeral))

maiorMedia = df["média"].max()
print("A maior média é:",(maiorMedia))
