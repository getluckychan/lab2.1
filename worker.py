import numpy as np


def read():
    try:
        set_elements1 = input("введіть елементи матриці a1 a2 a3: ")
        set_elements2 = input("введіть елементи матриці b1 b2 b3: ")
        set_elements3 = input("введіть елементи матриці c1 c2 c3: ")
        matrix = [[set_elements1], [set_elements2], [set_elements3]]
        print(matrix)
    except:
        print("Дотримуйтесь інструкцій")


matrix_elements = read()
print(matrix_elements)


def display():
    print(matrix_elements)
