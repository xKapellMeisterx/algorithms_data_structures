# Формат ввода
# В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули).
# Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.
# Пример ввода:
# 5
# 0 1 4 9 0

# Правильный ответ:
# 0 1 2 1 0

# Пример ввода:
# 6
# 0 7 9 4 8 20

# Правильный ответ:
# 0 1 2 3 4 5

# Формат вывода
# Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

def nearest_zero(houses: list) -> str:
    output: list = [0] * len(houses)
    zeroes: list = [
        index for index, value in enumerate(houses) if not value
    ]
    for zero in range(zeroes[0]):
        output[zero]: int = zeroes[0] - zero
    for zero in range(len(zeroes) - 1):
        for position in range(zeroes[zero] + 1, zeroes[zero + 1]):
            output[position]: int = min(
                position - zeroes[zero],
                zeroes[zero + 1] - position
            )
    for zero in range(zeroes[-1] + 1, len(houses)):
        output[zero]: int = zero - zeroes[-1]
    return ' '.join(str(x) for x in output)


if __name__ == "__main__":
    street_length = int(input())
    houses = list(map(int, input().split()))
    print(nearest_zero(houses))
