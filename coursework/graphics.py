import matplotlib.pyplot as plt
import numpy as np
from math import factorial
"""
Воспроизведение графиков вероятностных характеристик 
в зависимости от изменения стартовых характеристик
"""


def main():
    n = int(input('введите число каналов обслуживания: '))
    l = int(input('введите интенсивность входяшего потока: '))
    h = int(input('введите производительность канала: '))
    m = int(input('введите максимальную длину очереди: '))

    x = np.linspace(1, 10, 10)
    y1, y2, y3 = [], [], []
    for l in x:
        P = l / h
        w = P / n

        #1
        P0 = 0
        if w == 1:
            for k in range(n + 1):
                P0 += n ** k / factorial(k)
            P0 += n ** n / factorial(n) * m
            P0 = P0 ** -1
        else:
            for k in range(n + 1):
                P0 += n ** k / factorial(k) * w ** k
            P0 += n ** n / factorial(n) * (w ** (n + 1) * (1 - w ** m)) / (1 - w)
            P0 = P0 ** -1
        P = [P0, ]
        for k in range(1, n + 1):
            P.append((n ** k / factorial(k)) * w ** k * P[0])
        Nоч = 0
        for k in range(n + 1, n + 1 + m):
            Nоч += (k - n) * P[k]
        y1.append(Nоч)

        #2
        Nоч = 0
        if w == 1:
            Nоч = m * (m + 1) / (2 * (m + 2))
        else:
            Nоч = w ** 2 * (1 - w ** m * (m + 1 - m * w)) / ((1 - w ** (m + 2)) * (1 - w))
        y2.append(Nоч)

        #3
        Nоч = 0
        if w == 1:
            Nоч = m * (m + 1) / (2 * (n + m + 1))
        else:
            Nоч = w ** (n + 1) * (1 - w ** m * (m + 1 - m * w)) / ((1 - w ** (n + m + 1)) * (1 - w))
        y3.append(Nоч)

    plt.plot(x, y1, linestyle="-")
    plt.plot(x, y2, linestyle="-.")
    plt.plot(x, y3, linestyle=":")
    plt.xlabel("число каналов обслуживания")
    # plt.xlabel("максимальная длина очереди")
    # plt.xlabel("интенсивность входяшего потока")
    # plt.xlabel("производительность канала")
    plt.ylabel("среднее число заявок в очереди")
    plt.title("Зависимость среднего числа заявок в очереди\nот числа каналов обслуживания")
    plt.show()


if __name__ == "__main__":
    main()
