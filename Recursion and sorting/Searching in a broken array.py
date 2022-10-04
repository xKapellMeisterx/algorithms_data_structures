# Формат ввода
# Функция принимает массив натуральных чисел и искомое число k. Длина массива не превосходит
# 10000. Элементы массива и число k не превосходят по значению 10000.
# В примерах: В первой строке записано число n –— длина массива. Во второй строке записано положительное число k –— искомый элемент.
# Далее в строку через пробел записано n натуральных чисел – элементы массива.
# Пример ввода:

# 9
# 5
# 19 21 100 101 1 4 5 7 12

# Правильный ответ:
# 6

# Пример ввода:

# 2
# 1
# 5 1

# Правильный ответ:
# 1

# Формат вывода
# Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля).
# Если элемент не найден, функция должна вернуть − 1. Изменять массив нельзя.
# Для отсечения неэффективных решений ваша функция будет запускаться от
# 100000 до 1000000 раз.

from typing import List


def broken_search(nums: List[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right: int = mid - 1
            else:
                left: int = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left: int = mid + 1
            else:
                right: int = mid - 1
    return -1


if __name__ == '__main__':
    n: int = int(input())
    target: int = int(input())
    nums: list = [int(x) for x in input().split()]
    print(broken_search(nums, target))
