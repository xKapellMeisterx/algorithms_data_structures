# Формат ввода
# В первой строке дано целое число k (1 ≤ k ≤ 5).#
# В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.
# Примеры ввода:
# 3
# 1231
# 2..2
# 2..2
# 2..2

# Правильный ответ:
# 2

# Примеры ввода:
# 4
# 1111
# 9999
# 1111
# 9911

# Правильный ответ:
# 1

# Формат вывода
# Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.

def sleight_of_hand(keys_G_T: int, list_nums: list):
    num: int = 1
    result: int = 0
    while num <= 9:
        count_num: int = list_nums.count(str(num))
        if 0 < count_num <= keys_G_T:
            result += 1
        num += 1
    return result


if __name__ == "__main__":
    keys_G_T: int = int(input()) * 2
    list_nums: list = sum([x for x in (list(input()) for i in range(4))], [])
    result = sleight_of_hand(keys_G_T, list_nums)
    print(result)
