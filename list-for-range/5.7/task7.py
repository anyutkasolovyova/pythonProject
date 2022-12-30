if __name__ == '__main__':
    july_temperatures = [15, 17, 17, 13, 8, 12, 12, 12, 9, 15, 8, 10, 11, 9, 13, 9, 8, 11, 9, 16, 7, 12, 14, 10, 7, 16,
                         13, 12, 7, 12, 15]

    new_july_temperatures = []

    for index in range(len(july_temperatures)):  # ваш код здесь
        new_july_temperatures.append(july_temperatures[index] + 10)

    print(july_temperatures)
    print(new_july_temperatures)
