import random
from util import Util

class Cromossomo:

    def __init__(self, palavra, estado_final):
        self.palavra = palavra
        self.aptidao = self.calcular_aptidao(estado_final)

    # Representa a heuristica dinamica da solucao
    def calcular_aptidao(self, estado_final):
        nota = 0
        for i in range(len(estado_final)):
            if(estado_final[i] in self.palavra):
                nota += 5

            if(self.palavra[i] == estado_final[i]):
                nota += 50

        return nota
    
    def __str__(self):
        return f'{self.palavra} - {self.aptidao}'
    
    def __eq__(self, other):
        if isinstance(other, Cromossomo):
            return self.palavra == other.palavra
        return False

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for i in range(tamanho_populacao):
            palavra_gerada = Util.gerar_palavra(len(estado_final))
            individuo = Cromossomo(palavra_gerada, estado_final)
            populacao.append(individuo)

    @staticmethod
    def exibir_populacao(populacao, numero_geracao):
        print('Geracao...', numero_geracao)
        for individuo in populacao:
            print(individuo)

    @staticmethod
    def selecionar(populacao, nova_populacao, taxa_selecao):
        # Definir quantos serao selecionados
        # len(tamanho)              - 100
        # quantidade_selecionados   - taxa selecao
        quantidade_selecionados = int(len(populacao) * taxa_selecao / 100)

        torneio = list()

        # Elitismo
        nova_populacao.append(populacao[0])

        i = 1
        while(i < quantidade_selecionados):
            c1 = populacao[random.randrange(len(populacao))]

            while(True):
                c2 = populacao[random.randrange(len(populacao))]
                if not c1.__eq__(c2):
                    break

            while(True):
                c3 = populacao[random.randrange(len(populacao))]
                if not c3.__eq__(c1) and not c3.__eq__(c2):
                    break

            torneio.append(c1)
            torneio.append(c2)
            torneio.append(c3)

            torneio.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
            if torneio[0] not in nova_populacao:
                nova_populacao.append(torneio[0])
                i += 1

            torneio.clear()
   
    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        # Definir a quantidade de reproduzidos
        # len(populacao)            - 100
        # quantidade_reproduzidos   - taxa_reproducao
        quantidade_reproduzidos = int(len(populacao) * taxa_reproducao / 100)

        for i in range(int(quantidade_reproduzidos/2)+1):
            # Sorteia um pai entre os primeiros 20% da populacao
            cromossomo_pai = populacao[random.randrange(len(populacao))]

            while (True):
                cromossomo_mae = populacao[random.randrange(len(populacao))]
                if not cromossomo_pai.__eq__(cromossomo_mae):
                    break

            pai = cromossomo_pai.palavra
            mae = cromossomo_mae.palavra

            primeira_metade_pai = pai[0 : int(len(pai)/2)]
            segunda_metade_pai = pai[int(len(pai)/2) : len(pai)]

            primeira_metade_mae = mae[0 : int(len(mae)/2)]
            segunda_metade_mae = mae[int(len(mae)/2) : len(mae)]

            filho1 = primeira_metade_pai + segunda_metade_mae
            filho2 = primeira_metade_mae + segunda_metade_pai

            nova_populacao.append(Cromossomo(filho1, estado_final))
            nova_populacao.append(Cromossomo(filho2, estado_final))

            # Podar os excedentes
            while(len(nova_populacao) > len(populacao)):
                nova_populacao.pop()

    @staticmethod
    def mutar(populacao, estado_final):
        quantidade_mutantes = random.randrange(1, int(len(populacao) / 5))

        for i in range(quantidade_mutantes):
            mutante = populacao[random.randrange(50, len(populacao))]
            print('antes da mutacao...', mutante)
            # Posicao aleatoria
            posicao_gene_mutante = random.randrange(int(len(mutante.palavra)))
            # Letra aleatoria
            novo_gene = Util.letras[random.randrange(Util.tamanho)]
            # Troca a letra na palavra
            mutante.palavra[posicao_gene_mutante].replace(str(novo_gene))
            # Calcula aptidao
            mutante.calcular_aptidao(estado_final)
            print('depois da mutacao...', mutante)