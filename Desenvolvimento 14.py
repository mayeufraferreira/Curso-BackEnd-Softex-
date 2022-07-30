print ("Descubra qual a melhor categoria de habilitação para o seu veículo!")
rodas = int(input("Informe a quantidade de rodas: "))
peso = int(input("Informe o peso do veículo (bruto, em kg): "))
pessoas = int(input("Informe quantas pessoas cabem no veículo: "))
 
if rodas <=3:
   print ("Categoria A!")
elif rodas==4 and pessoas<=8 and peso<=3500:
   print ("Categoria B!")
elif rodas>=4 and peso>=3500 and peso<=6000:
   print ("Categoria C!")
elif rodas>=4 and pessoas>8:
   print ("Categoria D!")
elif rodas>=4 and peso>6000:
   print ("Categoria E!")