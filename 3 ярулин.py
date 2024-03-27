# Импорт необходимых модулей
from functools import reduce
from math import sqrt

# Пункт 1: Изучение элементов языка

# Пункт 2: Вычисление степеней элементов списка
numbers = [i for i in range(1, 51)]
powers = [[num**exp for exp in range(4, 7)] for num in numbers]
print("Powers:", powers)

# Пункт 3: Транспонирование матрицы
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed Matrix:", transposed_matrix)

# Пункт 4: Фильтрация чисел, делящихся на 36
divisible_by_36 = list(filter(lambda x: x % 36 == 0, range(-9999, 10000)))
print("Numbers divisible by 36:", divisible_by_36)

# Пункт 5: Редактирование заголовков в англоязычном стиле
def edit_titles(sentence):
    return ' '.join(map(lambda word: word.capitalize() if len(word) > 3 else word, sentence.split()))

print("Edited Title:", edit_titles("the quick brown fox jumps over the lazy dog"))

# Пункт 6: Максимальная длина шестизвенного манипулятора
class ManipulatorJoint:
    def __init__(self, position=0):
        self.position = position

class SixAxisManipulator:
    def __init__(self):
        self.joints = [ManipulatorJoint() for _ in range(6)]

max_length = reduce(lambda acc, joint: acc + joint.position, SixAxisManipulator().joints, 0)
print("Max Length of Manipulator:", max_length)

# Пункт 7: Частичное выполнение функции
from functools import partial

def foo(a:int, b:int, c:int, d:int) -> int:
    return a*4 + b*3 + c*2 + d

partial_foo = partial(foo, b=15, c=30, d=45)
print("Partial Function Result:", partial_foo(5))

# Пункт 8: Сумма квадратов чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
fibonacci_numbers = [next(fib) for _ in range(50)]

squares_sum = sum(map(lambda x: x**2, fibonacci_numbers[:10]))
print("Sum of Squares of First 10 Fibonacci Numbers:", squares_sum)

# Пункт 9: Генератор аэропортов
def airports_generator():
    airports = [
        {'IATA': 'ATL', 'Name': 'Hartsfield-Jackson Atlanta International Airport', 'Location': 'Atlanta, Georgia, United States'},
        {'IATA': 'PEK', 'Name': 'Beijing Capital International Airport', 'Location': 'Chaoyang-Shunyi, Beijing, China'},
        {'IATA': 'LHR', 'Name': 'London Heathrow Airport', 'Location': 'Hillingdon, London, United Kingdom'}
        # Здесь можно добавить остальные аэропорты
    ]
    for airport in airports:
        yield airport

# Пункт 10: Сохранение в текстовый файл
with open("airports.txt", "w") as file:
    for airport in airports_generator():
        file.write(f"{airport['IATA']}\t{airport['Name']}\n")
