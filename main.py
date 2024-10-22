class StepValueError(ValueError):
    """Пользовательский класс исключений,
    наследуется от класса ValueError"""
    pass

class Iterator:
    """Класс-итератор. Генерирует последовательность чисел,
    начиная с числа start до числа stop включительно
    с шагом step"""

    def __init__(self, start, stop, step=1):
        """Конструктор класса."""
        if step == 0:
            raise StepValueError()
        """Если шаг отличен от нуля, создаем и инициализируем атрибуты объекта класса"""
        self.start = start
        self.stop = stop
        self.step = step


    def __iter__(self):
        """Магический метод устанавливает указатель
        и возвращает ссылку на объект класса"""
        self.pointer = self.start - self.step
        return self


    def __next__(self):
        """Магический метод проверяет, выходи ли следующее генерируемое значение
        за пределы, обозначенные числом stop.
        Если следующее генерируемое значение выходит за пределы числа stop,
        создается исключение StopIteration и генерация чисел прекращается,
        иначе возвращается следующее генерируемое значение"""
        if self.step > 0:   # если step > 0
            if self.pointer + self.step > self.stop:
                raise StopIteration
        else:   # если step < 0
            if self.pointer + self.step < self.stop:
                raise StopIteration
        """Если исключение не сработало, генерируем и возвращает следующее значение """
        self.pointer += self.step
        return self.pointer


# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()