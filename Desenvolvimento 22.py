class Cliente:
    
    incremento = 0
 
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def Cadastrar(self):
            print("Nome:",self.nome)
            print("Email:",self.email)
            print("Cadastro efetivado com sucesso!")
            Incrementar()
            
    def Incrementar():
        Cliente.incremento += 1
        

c1 = Cliente("Cliente 1", "cliente1@gmail.com")
c1.Cadastrar()

c2 = Cliente("Cliente 2", "cliente2@gmail.com")
c2.Cadastrar()

c3 = Cliente("Cliente 3", "cliente3@gmail.com")
c3.Cadastrar()

Cliente.Incrementar()

c1.incremento()
c2.incremento()
c3.incremento()