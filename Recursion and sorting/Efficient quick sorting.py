# Формат ввода
# В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
# В каждой из следующих n строк задана информация про одного из участников.
# i-й участник описывается тремя параметрами:
# уникальным логином (строкой из маленьких латинских букв длиной не более 20)
# числом решённых задач Pi
# штрафом Fi
# Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

# Пример ввода:

# 5
# alla 4 100
# gena 6 1000
# gosha 2 90
# rita 2 90
# timofey 4 80

# Правильный ответ:
# gena
# timofey
# alla
# gosha
# rita

# Пример ввода:

# 5
# alla 0 0
# gena 0 0
# gosha 0 0
# rita 0 0
# timofey 0 0

# Правильный ответ:
# alla
# gena
# gosha
# rita
# timofey

# Формат вывода
# Для отсортированного списка участников выведите по порядку их логины по одному в строке.

def qsort(arr: list, left: int, right: int) -> None:
    if right <= left:
        return
    left_idx: int = left
    right_idx: int = right
    pivot: int = (left + right) // 2
    reference: list = arr[pivot]
    while left_idx <= right_idx:
        while reference > arr[left_idx]:
            left_idx += 1
        while reference < arr[right_idx]:
            right_idx -= 1
        if left_idx <= right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
            left_idx += 1
            right_idx -= 1

    qsort(arr, left, right_idx)
    qsort(arr, left_idx, right)


def get_order(players: list) -> list:
    qsort(players, 0, len(players) - 1)
    return (row[2] for row in players)


def main():
    count_line: int = int(input())
    persons: list = [None] * count_line
    for incoming_data in range(count_line):
        name, points, penalty = input().split()
        persons[incoming_data] = (-int(points), int(penalty), name)
    result: list = get_order(persons)
    print(*result, sep='\n')


if __name__ == '__main__':
    main()
