class Porta:
    def __init__(self, altura, cor, material):
        self.altura = altura
        self.cor = cor
        self.material = material

    def Bater(self):
        print("Toc-Toc")

    def Abrir(self):
        print("Porta aberta")

    def Fechar(self):
        print("Porta fechada")


class Livro:
    def __init__(self,titulo,genero,autor):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor

    def MarcarPagina(self):
        print("Página marcada!")

    def PassarParaProximaPagina(self):
        print("Passando para próxima página")

    def VoltarParaPaginaAnterior(self):
        print("Voltando à página anterior")


class Paciente:
    def __init__(self,pa,temperatura,glicemia):
        self.pa = pa
        self.temperatura = temperatura
        self.glicemia = glicemia

    def AferirPA(self):
        print("Pressão arterial do paciente:",self.pa)

    def VerTemperatura(self):
        print("Temperatura do paciente:",self.temperatura)

    def MedirGlicemia(self):
        print("Glicemia do paciente:",self.glicemia)


class Video:
    def __init__(self,duracao,qualidade,formato):
        self.duracao = duracao
        self.qualidade = qualidade
        self.formato = formato

    def Pausar(self):
        print("Vídeo pausado")

    def AtivarLegendas(self):
        print("Legendas ativadas")

    def Play(self):
        print("Vídeo em reprodução")
