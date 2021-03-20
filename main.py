import numpy as np
import matplotlib.pyplot as plt


def main():
    x = [-20, -3, -4, 0, 1, 5, 6, 7, 20]
    x.sort()

    y = [function(value) for value in x]

    x_triplets = build_triplets(x)
    y_triplets = build_triplets(y)

    x_general = []
    lagr = []

    for i in range(len(x_triplets)):
        x_new = np.linspace(x_triplets[i][0], x_triplets[i][-1], 50)
        x_general.extend(x_new)
        if len(x_triplets[i]) == 2:
            additional_x = (x_triplets[i][0] + x_triplets[i][1]) / 2
            additional_y = function(additional_x)
            x_triplets[i].insert(1, additional_x)
            y_triplets[i].insert(1, additional_y)
        for j in x_new:
            lagr.append(lagrange(y_triplets[i], x_triplets[i], j))

    plt.plot(x, y, 'o', x_general, lagr)
    plt.show()


def function(value):
    return np.cos(value)


def build_triplets(x: list):
    triplets = []
    for i in range(0, len(x), 2):
        if i == 0:
            continue

        triplets.append([x[i - 2], x[i - 1], x[i]])

    if x[-1] not in triplets[-1]:
        triplets.append([triplets[-1][2], x[-1]])

    return triplets


def lagrange(y_triplet, x_triplet, x):
    return y_triplet[0] * ((x - x_triplet[1]) * (x - x_triplet[2])) / (
                (x_triplet[0] - x_triplet[1]) * (x_triplet[0] - x_triplet[2])) \
           + y_triplet[1] * ((x - x_triplet[0]) * (x - x_triplet[2])) / (
                       (x_triplet[1] - x_triplet[0]) * (x_triplet[1] - x_triplet[2])) \
           + y_triplet[2] * ((x - x_triplet[0]) * (x - x_triplet[1])) / (
                       (x_triplet[2] - x_triplet[0]) * (x_triplet[2] - x_triplet[1]))


if __name__ == '__main__':
    main()
