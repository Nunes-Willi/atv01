
#TODO 06
class Usuario:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def hello(self):
        return("Olá")

#TODO 07, 08, 09 e 10
usuario1 = Usuario("Patrick" , "Jane", 43)
usuario2 = Usuario("Red", "Jhon", 56)

print(usuario1.hello())
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.idade)

print(f"{usuario1.hello()}, {usuario1.nome} {usuario1.sobrenome}")
print(f"{usuario1.hello()}, {usuario2.nome} {usuario2.sobrenome}")
