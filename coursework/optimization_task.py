from math import factorial
import numpy as np
"""
Задача оптимизации сформулирована следующим образом:
Необходимо подобрать число каналов обслуживания
таким образом, чтобы затраты оказались минимальными.
"""


def f1(N, m, h, l, d1, d2):
    Nоч = 0
    W = []
    for n in range(1, N+1):
        Nоч = 0
        P = l / h
        w = P / n
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
        for k in range(n + 1, n + m + 1):
            P.append((n ** n / factorial(n)) * w ** k * P[0])
        P.append((n ** n / factorial(n)) * w ** (n+m) * P0)
        K = (l * (1 - (n ** n / factorial(n)) * w ** (m+n) * P0)) / h  # среднее число занятых каналов

        for k in range(n + 1, n + 1 + m):
            Nоч += (k - n) * P[k]
        W.append(d1*Nоч + d2*K)
    print('минимум на ', np.argmin(W) + 1, 'линии')


def f2(N, m, h, l, d1, d2):
    W = []
    for n in range(1, N + 1):
        P = l / h
        w = P / n
        P0 = 0
        if w == 1:
            P0 = 1 / (m + 2)
        else:
            P0 = (1 - w) / (1 - w ** (m + 2))
        K = n * (1 - P0)
        if w == 1:
            Nоч = m * (m + 1) / (2 * (m + 2))
        else:
            Nоч = w ** 2 * (1 - w ** m * (m + 1 - m * w)) / ((1 - w ** (m + 2)) * (1 - w))
        W.append(d1 * Nоч + d2 * K)
    print('минимум на ', np.argmin(W) + 1, 'линии')


def f3(N, m, h, l, d1, d2):
    W = []
    for n in range(1, N + 1):
        P = l / h
        w = P / n
        P0 = 0
        for k in range(n + m + 1):
            P0 += w ** k
        P0 = P0 ** -1
        K = l * (1 - P0 * w ** (m + n)) / h
        if w == 1:
            Nоч = m * (m + 1) / (2 * (n + m + 1))
        else:
            Nоч = w ** (n + 1) * (1 - w ** m * (m + 1 - m * w)) / ((1 - w ** (n + m + 1)) * (1 - w))
        W.append(d1 * Nоч + d2 * K)
    print('минимум на ', np.argmin(W) + 1, 'линии')


def main():
    a = int(input('введите ограничение на количество линий обслуживания: '))
    l = int(input('введите интенсивность входяшего потока: '))
    h = int(input('введите производительность канала: '))
    m = int(input('введите максимальную длину очереди: '))
    d1 = int(input('введите затраты на пребывание заявки в очереди: '))
    d2 = int(input('введите затраты на обслуживание заявки: '))
    print('для СМО с ожиданием и ограничением на длину очереди')
    f1(a, m, h, l, d1, d2)
    print('для СМО с ожиданием и ограничением на длину очереди и взаимопомощью между каналами типа «все как один»')
    f2(a, m, h, l, d1, d2)
    print('для СМО с ожиданием и ограничением на длину очереди и «равномерной» взаимопомощью между каналами')
    f3(a, m, h, l, d1, d2)


if __name__ == "__main__":
    main()
