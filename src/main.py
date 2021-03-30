import math
import numpy
from matplotlib import pyplot as plt


def func_x(y):
    x = 0.7 - math.cos(y - 1)
    return x


def func_y(x):
    y = 1 - math.sin(x) / 2
    return y


def draw_graph(a, b, n):
    x_arr, y_arr = [], []
    dot_count = numpy.linspace(a, b, n)
    for i in dot_count:
        x_arr.append(func_x(i))
        y_arr.append(func_y(i))
    plt.plot(x_arr, dot_count, dot_count, y_arr)
    plt.grid()
    plt.show()


def system_solution(accuracy, x_0, y_0):
    x = func_x(y_0)
    y = func_y(x_0)
    k = 1
    while (abs(x - x_0) > accuracy) or (abs(y - y_0) > accuracy):
        x_0 = x
        y_0 = y
        x = func_x(y_0)
        y = func_y(x_0)
        k += 1
    print(f"Количество итераций: {k}\n"
          f"Решение: x = {x}, y = {y}\n"
          f"deltaX = {x - x_0}\n"
          f"deltaY = {y - y_0}\n"
          f"f1 = {func_x(y) - x}\n"
          f"f2 = {func_y(x) - y}")


draw_graph(-5, 5, 150)
x_graph = 0
y_graph = 1
system_solution(0.01, x_graph, y_graph)
