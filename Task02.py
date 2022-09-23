# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

def check_equality(x, y, z):
    left = not(x or y or z)
    print('left =', left)
    right = not x and not y and not z
    print('right =', right)
    print('Истинность left = right:', left == right)

a = input("X: ")
b = input("Y: ")
c = input("Z: ")
check_equality(a, b, c)