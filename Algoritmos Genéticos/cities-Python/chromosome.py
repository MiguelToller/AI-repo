import random

from util import Util

class Chromosome:

    def __init__(self, city, final_state):
        self.city = city
        self.fitness = self.calculate_fitness(final_state)

    def calculate_fitness(self, final_state):
        penalty = 0

        # Penalty for incorrect order
        for i in range(len(final_state) - 1):
            if(self.city[i] > self.city[i+1]):
                penalty += 10

        # Count occurrences of each city
        counts = {}
        for city in self.city:
            if city in counts: 
                counts[city] += 1
            else: 
                counts[city] = 1

        # Penalty for repeated cities
        for count in counts.values():
            if count > 1:
                num_pairs = (count * (count - 1)) // 2
                penalty += num_pairs * 20

        return penalty
    
    def __str__(self):
        return f'{self.city} - {self.fitness}'
    
    def __eq__(self, other):
        if isinstance(other, Chromosome):
            return self.city == other.city
        return False
    
    @staticmethod
    def generate_cities(cities, num_cities, final_state):
        for i in range(num_cities):
            new_city = Util.generate_city(len(final_state))
            individual = Chromosome(new_city, final_state)
            cities.append(individual)

    @staticmethod
    def show_cities(cities, generation):
        print('Generation...', generation)
        for individual in cities:
            print(individual)

    @staticmethod
    def tournament_selection(cities, new_cities, selection_rate):
        num_selected = int(len(cities) * selection_rate / 100)

        tournament = list()

        # Elitism
        new_cities.append(cities[0])

        i = 1
        while(i < num_selected):
            s1 = cities[random.randrange(len(cities))]

            while(True):
                s2 = cities[random.randrange(len(cities))]
                if not s1.__eq__(s2):
                    break

            while(True):
                s3 = cities[random.randrange(len(cities))]
                if not s3.__eq__(s1) and not s3.__eq__(s2):
                    break

            tournament.append(s1)
            tournament.append(s2)
            tournament.append(s3)

            tournament.sort(key=lambda chromosome: chromosome.fitness, reverse=False)
            if tournament[0] not in new_cities:
                new_cities.append(tournament[0])
                i += 1

            tournament.clear()

    @staticmethod
    def reproduction(cities, new_cities, reproduction_rate, final_state):
        num_reproduced = int(len(cities) * reproduction_rate / 100)

        for i in range(int(num_reproduced/2)+1):
            # Select a random parent from the top 20% of the population
            chromosome_father = cities[random.randrange(len(cities))]

            while(True):
                chromosome_mother = cities[random.randrange(len(cities))]
                if not chromosome_father.__eq__(chromosome_mother):
                    break

            father = chromosome_father.city
            mother = chromosome_mother.city

            first_half_father = father[:len(father)//2]
            second_half_father = father[len(father)//2 : len(father)]

            first_half_mother = mother[:len(mother)//2]
            second_half_mother = mother[len(mother)//2 : len(mother)]

            chield1 = first_half_father + second_half_mother
            chield2 = first_half_mother + second_half_father

            new_cities.append(Chromosome(chield1, final_state))
            new_cities.append(Chromosome(chield2, final_state))

            # Trim the excess
            while(len(new_cities) > len(cities)):
                new_cities.pop()

    @staticmethod
    def mutate(cities, final_state):
        num_mutants = random.randrange(1, int(len(cities) / 5))

        while(num_mutants > 0):
            mutant_position = random.randrange(int(len(cities)))
            mutant = cities[mutant_position]
            print('\nMutating...', mutant)

            # Changing
            mutant_city = mutant.city
            # Random position
            mutant_caracter = mutant.city[random.randrange(len(mutant.city))]
            # Random number
            sorted_caracter = Util.numbers[random.randrange(Util.size)]
            # Change the number in the array
            mutant_city = mutant_city.replace(mutant_caracter, sorted_caracter)

            mutant = Chromosome(mutant_city, final_state)
            cities[mutant_position] = mutant
            num_mutants -= 1