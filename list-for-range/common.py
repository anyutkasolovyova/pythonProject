if __name__ == '__main__':
    dangerous_animals = ['волк', 'медведь', 'тигр', 'крокодил', 'леопард', 'бегемот', 'удав', 'тираннозавр', 'лев']

    for i in range(len(dangerous_animals)):
        print(i, dangerous_animals[i])

    # то же самое
    for animal in dangerous_animals:
        print(animal)
