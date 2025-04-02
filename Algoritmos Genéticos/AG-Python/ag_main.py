from cromossomo import Cromossomo

estado_final = input('Entre com a palavra do estado final: ')
tamanho_populacao = int(input('Tamanho da populacao: '))
quantidade_geracoes = int(input('Geracoes: '))
taxa_selecao = int(input('Taxa de selecao [25 a 25]: '))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input('Taxa de mutacao: '))

populacao = list()
nova_populacao = list()

Cromossomo.gerar_populacao(populacao, tamanho_populacao, estado_final)
populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
Cromossomo.exibir_populacao(populacao, 0)

for i in range(1, quantidade_geracoes):
    Cromossomo.selecionar(populacao, nova_populacao, taxa_reproducao)
    Cromossomo.reproduzir(populcao, nova_populacao, taxa_reproducao)

    if i % taxa_mutacao == 0:
        Cromossomo.mutar(nova_populacao)

    populacao.clear
    populacao.append(nova_populacao)
    nova_populacao.clear
    populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
    Cromossomo.exibir_populacao(populacao, i)