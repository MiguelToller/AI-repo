from util import Util

class Cromossomo:

    def __init__(self, palavra, estado_final):
        self.palavra = palavra
        self.aptidao = self.calcular_aptidao(estado_final)

    def calcular_aptidao(self):
        pass

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for i in range(tamanho_populacao):
            palavra_gerada = Util.gerar_palavra(len(estado_final))


        

