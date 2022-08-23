class Aluno:
    def __init__(self,nome,media):
        self.__nome = nome
        self.__media = media

    def getNome(self):
        return self.__nome

    def getMedia(self):
        return self.__media

    def setMedia(self):
        self.novaMedia = float(self.__media) + 1
        return self.novaMedia

    def Situacao(self):
        if self.novaMedia >= 7:
            print("Situação do(a) aluno(a): Aluno(a) aprovado(a)")
        else:
            print("Situação do(a) aluno(a): Aluno(a) reprovado(a)")


a1 = Aluno("Aluno 1", "6.5")
print("Nome do(a) aluno(a):",a1.getNome())
print("Primeira média:",a1.getMedia())
print("Média ajustada:", a1.setMedia())
a1.Situacao()
