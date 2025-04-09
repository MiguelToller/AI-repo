import random

class Util:

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    size = len(numbers)

    @staticmethod
    def generate_city(size):
        city = ''
        for i in range(size):
            city += str(Util.numbers[random.randrange(Util.size)])

        return city