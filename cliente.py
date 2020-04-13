class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome
    
    @property #chama o método get
    def nome(self):
        print("chamando o @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        print("chamando o setter nome()")
        self.__nome = novo_nome
