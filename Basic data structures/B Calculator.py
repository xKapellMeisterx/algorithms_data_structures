# Формат ввода
# В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны через пробел.
# На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
# Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

# Примеры ввода:
# 2 1 + 3 *

# Правильный ответ:
# 9

# Примеры ввода:
# 7 2 + 4 * 2 +

# Правильный ответ:
# 38

# Формат вывода
# Выведите единственное число — значение выражения.

import operator


def evalRPN(symbol: dict, tokens: list) -> int:
    stack: list = []
    if not len(tokens):
        return 0
    for a in tokens:
        if a not in symbol:
            stack.append(a)
        else:
            b: int = int(stack.pop())
            c: int = int(stack.pop())
            if a in symbol:
                stack.append(symbol[a](c, b))
    return int(stack[-1])


if __name__ == '__main__':
    list_in: list = input().split()
    symbol: dict = {
        "+": operator.add,
        "-": operator.sub,
        '/': operator.floordiv,
        '*': operator.mul,
    }
    print(evalRPN(symbol, list_in))





