class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
    def __str__(self):
        return f'{self.txt}'

inp_data = int(input('Первое число '))
inp_data2 = int(input('Второе число '))

try:
    inp_data = int(inp_data)
    inp_data2 = int(inp_data2)

    z = inp_data / inp_data2

except ZeroDivisionError:
    c = OwnError('Была ошибка')
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {z}")


"""
1. Небольшой косяк с отступами (строка 4 и 7), между методами класса должна быть минимум одна пустая строка,
а между вокруг классов, функций и импортов - минимум две.
2. Две бесполезные строки, дублирующие приведение введенных данных к числовому типу (7 и 8).
3. Вообще, если пройдена тема try/except, вполне можно обработать и введение данных, в случае если пользователь
введет что-то, отличное от чисел.
4. Исходя из предыдущего пункта, если пользователь введет не числа - программа упадет с ошибкой, не добравшись 
до обработки ValueError.
5. Когда отлавливается ZeroDivisionError, студент создает экземпляр класса OwnError, тогда как нужно было
было возбудить исключение через raise.
6. Вообще, не обязательно переопределять в своих классах-исключениях дандеры __init__ и __str__ - можно обойтись
pass, Python сам выведет нужный текст ошибки, если ввести его в скобках после исключения.
"""
