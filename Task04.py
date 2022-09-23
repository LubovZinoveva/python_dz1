 # Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
 # первое число, второе число и операцию, после чего применяет операцию к введённым числам 
 # ("первое число" "операция" "второе число") и выводит результат на экран.

def calculator(a, b, operation):
    if operation == 'div':
        if b == 0:
            return 'Деление на 0!'
        else:
            return a // b 
    elif operation == '/':
        if b == 0:
            return 'Деление на 0!'
        else:
            return a / b 
    elif operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == 'mod':
        if b == 0:
            return 'Деление на 0!'
        else:
            return a % b
    elif operation == 'pow':
        c = a
        for i in range(1, b+1):
            c *= a
        return c
    else:
        return 'Можно выполнить только: + - / * mod pow div'

try:
    number_1 = float(input('Первое число: '))
    number_2 = float(input('Второе число: '))
    action = input('Действие: ')
    print(calculator(number_1, number_2, action))
except:
    print('Ошибка, введите 2 вещественных числа и действие')
