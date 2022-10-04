# Формат ввода
# В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека.
# Он не превосходит 50000. В следующих n строках записана одна из команд:
# push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
# push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
# pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
# pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
# Value — целое число, по модулю не превосходящее 1000.

# Примеры ввода:

# 4
# 4
# push_front 861
# push_front -819
# pop_back
# pop_back

# Правильный ответ:
# 861
# -819

# Пример ввода:

# 7
# 10
# push_front -855
# push_front 0
# pop_back
# pop_back
# push_back 844
# pop_back
# push_back 823

# Правильный ответ:
# -855
# 0
# 844

# Формат вывода
# Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

ERROR = 'error'
RUNTIMEERROR = 'Достигнут максимальный размер дека.'


class Deque:
    def __init__(self, max_size: int):
        self.__items: list = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 1
        self.__tail: int = 0
        self.__size: int = 0

    def get_index(self, index: int, add: bool) -> int:
        index = index + 1 if add else index - 1
        return index % self.__max_size

    def is_empty(self):
        return self.__size == 0

    def is_size_max(self):
        return self.__size == self.__max_size

    def push_front(self, value):
        if self.is_size_max():
            raise RuntimeError(RUNTIMEERROR)
        self.__head: int = self.get_index(self.__head, False)
        self.__items[self.__head]: int = value
        self.__size += 1

    def push_back(self, value):
        if self.is_size_max():
            raise RuntimeError(RUNTIMEERROR)
        self.__tail: int = self.get_index(self.__tail, True)
        self.__items[self.__tail]: int = value
        self.__size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise RuntimeError(ERROR)
        value: int = self.__items[self.__head]
        self.__head: int = self.get_index(self.__head, True)
        self.__size -= 1
        return value

    def pop_back(self) -> int:
        if self.is_empty():
            raise RuntimeError(ERROR)
        value: int = self.__items[self.__tail]
        self.__tail: int = self.get_index(self.__tail, False)
        self.__size -= 1
        return value


if __name__ == '__main__':
    command_count: int = int(input())
    deque: object = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().split(' ')
            result = getattr(deque, command)(*params)
            if result is not None:
                print(result)
        except (RuntimeError, AttributeError):
            print(ERROR)
