import enum
from re import X
from tkinter import Y

class Candidato(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

votar = True
votosX = 0
votosY = 0
votosZ = 0
votosBrancos = 0
votosNulos = 0
while votar:
    votoInvalido = True
    voto = -1
    while votoInvalido:
        try:
            print("Digite 889 para votar no Candidato X")
            print("Digite 847 para votar no Candidato Y")
            print("Digite 515 para votar no Candidato Z")
            print("Caso deseja votar em branco digite 0")
            voto = int(input("Digite seu voto: "))
            votoInvalido = False
        except:
            print("Voto inválido, por favor, vote novamente.")

    
    op = True
    while op:
        print("_________________________________________")
        print("1.Sim")
        print("2.Não")
        opcao = int(input("Deseja encerrar a votação agora? "))
        print("_________________________________________")
        if opcao == 1:
            op = False
            votar = False
        elif opcao == 2:
            op = False
            votar = True
        else:
            print("Esta opção não existe, tente novamente.")
        
    
    if Candidato.candidato_X.value == voto:
        votosX += 1
    elif Candidato.candidato_Y.value == voto:
        votosY += 1
    elif Candidato.candidato_Z.value == voto:
        votosZ += 1
    elif Candidato.branco.value == voto:
        votosBrancos += 1
    else:
        votosNulos += 1
print("_________________________________________")
print("Votos para  o(a) candidato(a) {}: {}".format(Candidato.candidato_X.name, votosX))
print("Votos para  o(a) candidato(a) {}: {}".format(Candidato.candidato_Y.name, votosY))
print("Votos para  o(a) candidato(a) {}: {}".format(Candidato.candidato_Z.name, votosZ))
print("Votos brancos: {}".format(votosBrancos))
print("Votos nulos: {}".format(votosNulos))
print()

if (votosX > votosY) and (votosY >= votosZ):
    print("O vencedor da eleição foi o Candidato X!")
if (votosY > votosX) and (votosX >= votosZ):
    print("O vencedor da eleição foi o Candidato Y!")
if (votosZ > votosX) and (votosX >= votosY):
    print("O vencedor da eleição foi o Candidato Z!") 
   