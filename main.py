import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, ceil, floor
import matplotlib.lines as mlines

data = [
    50, 50, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200, 250, 250, 300, 300, 300, 300, 300,
    350, 350, 400, 400, 400, 450, 500, 500, 500, 500, 500, 500, 600, 700, 800, 800, 900, 950, 1000, 1000,
    1000, 1000, 1000, 1300, 1500, 1500, 1500, 2000, 2000, 2600, 3000
]


def mean(a):
    return sum(a) / len(a)


def med(a):
    return sorted(a)[len(a) // 2]


def S2(a):
    m = mean(a)
    return sum([(e - m) ** 2 for e in a]) / len(a)


def v_row(a):
    r = []
    for i in sorted(list(set(a))):
        r.append((i, len(list(filter(lambda x: x == i, a)))))
    return r


def D(a, price):
    return len(list(filter(lambda x: x >= price, a)))


def get_demands(a):
    v = v_row(a)
    r = []
    for price, _ in v:
        r.append((price, D(a, price)))
    return r


def get_profits(a, TC):
    ret = []

    for price, _ in v_row(a):
        if price < TC:
            ret.append((price, 0, 0))
        else:
            customers = D(a, price)
            profit = (price - TC) * customers
            ret.append((price, customers, profit))
    return ret


def get_max_profit(a, TC):
    profits = get_profits(a, TC)
    return max(profits, key=lambda x: x[2])


def main():
    # fig = plt.gcf()
    # fig.set_size_inches(8, 5)
    # plt.subplot()
    #
    # plt.plot(data, np.arange(start=len(data), stop=0, step=-1))
    #
    # plt.xlim([0, 3000])
    # plt.ylim([0, len(data) + 1])
    # plt.xlabel('Цена, руб')
    # plt.ylabel('Спрос')
    # plt.grid()
    #
    # plt.show()

    print('Вариационный ряд, элементов:', len(v_row(data)))
    for i in v_row(data):
        print(i)

    print()

    print('Цена / спрос')
    for i in get_demands(data):
        print(i)

    print()

    print('Прибыль при затратах')
    for i in [40, 200, 250, 350, 420]:
        print('Затраты:', i)
        for j in get_profits(data, i):
            print(j)
        print('Наибольшая прибыль:', get_max_profit(data, i))
        print()

    print('Границы смены оптимальной цены при различных затратах')
    was = set()
    for i in range(1, 2000):
        mm = get_max_profit(data, i)
        if mm[0] not in was:
            print(i, mm)
            was.add(mm[0])


if __name__ == '__main__':
    main()
