import random

class Util:

    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    tamanho = len(letras)
    
    @staticmethod
    def gerar_palavra(tamanho_palavra):
        palavra = ''
        for i in range(tamanho_palavra):
            palavra += Util.letras[random.randrange(Util.tamanho)] 

        return palavra