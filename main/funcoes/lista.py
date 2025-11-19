import random

class Lista():

    def gerar_lista():
        tamanho = int(input("Insira o tamanho da lista: "))
        lista = [random.randint(0,7) for i in range(tamanho)]
        return lista