from chromosome import Chromosome

final_state = '123456789'

num_cities = int(input('Number of cities: '))
num_generations = int(input('Generations: '))
selection_rate = int(input('Selection rate [25 to 25]: '))
mutation_rate = int(input('Mutation rate: '))
reproduction_rate = 100 - selection_rate

mutation_frequency = 100 - (num_cities * mutation_rate / 100)

cities = list()
new_cities = list()

Chromosome.generate_cities(cities, num_cities, final_state)
cities.sort(key=lambda chromosome : chromosome.fitness, reverse=False)
Chromosome.show_cities(cities, 0)

for i in range(1, num_generations):
    Chromosome.tournament_selection(cities, new_cities, selection_rate)
    Chromosome.reproduction(cities, new_cities, reproduction_rate, final_state)

    # Mutation breaks the local maximum
    if i % mutation_rate == 0:
        Chromosome.mutate(new_cities, final_state)

    cities.clear()
    cities.extend(new_cities)
    new_cities.clear()
    cities.sort(key=lambda chromosome: chromosome.fitness, reverse=False)
    Chromosome.show_cities(cities, i)