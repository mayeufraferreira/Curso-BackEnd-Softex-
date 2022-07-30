def calc(num1,num2,operacao):
   if operacao==1:
       return num1+num2
   if operacao==2:
       return num1-num2
   if operacao==3:
       return num1*num2
   if operacao==4:
       return num1/num2

execute=True
while execute:
   print("Operações:")
   print("1.Soma")
   print("2.Subtração")
   print("3.Multiplicação")
   print("4.Divisão")

   operacao=int(input("Qual operação você quer realizar? "))
   if operacao >=1 and operacao <=4:
       num1=float(input("Primeiro número: "))
       num2=float(input("Segundo número: "))

       resultado=calc(num1,num2,operacao)
       print("O resultado da sua operação é:",resultado)

   else:
       print("0")
