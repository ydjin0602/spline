import typing as t
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    x = [-20, -4, -3, 0, 1, 5, 6, 7, 20, 50]
    x.sort()

    y = [function(value) for value in x]

    x_triplets = build_triplets(x)
    y_triplets = build_triplets(y)

    x_general = []
    interpolant = []

    for i in range(len(x_triplets)):
        x_new = np.linspace(x_triplets[i][0], x_triplets[i][-1], 50)
        x_general.extend(x_new)
        if len(x_triplets[i]) == 2:
            additional_x = (x_triplets[i][0] + x_triplets[i][1]) / 2
            additional_y = (y_triplets[i][0] + y_triplets[i][1]) / 2
            x_triplets[i].insert(1, additional_x)
            y_triplets[i].insert(1, additional_y)
        for j in x_new:
            interpolant.append(lagrange(y_triplets[i], x_triplets[i], j))

    plt.plot(x, y, 'o', x_general, interpolant)
    plt.show()


def function(value: t.Union[int, float]) -> float:
    return np.cos(value)


def build_triplets(x: t.List[float]) -> t.List[t.List[float]]:
    triplets = []
    for i in range(0, len(x), 2):
        if i == 0:
            continue

        triplets.append([x[i - 2], x[i - 1], x[i]])

    if x[-1] not in triplets[-1]:
        triplets.append([triplets[-1][2], x[-1]])

    return triplets


def lagrange(y_triplet: t.List[float], x_triplet: t.List[float], x: float) -> float:
    return y_triplet[0] * ((x - x_triplet[1]) * (x - x_triplet[2])) / (
                (x_triplet[0] - x_triplet[1]) * (x_triplet[0] - x_triplet[2])) \
           + y_triplet[1] * ((x - x_triplet[0]) * (x - x_triplet[2])) / (
                       (x_triplet[1] - x_triplet[0]) * (x_triplet[1] - x_triplet[2])) \
           + y_triplet[2] * ((x - x_triplet[0]) * (x - x_triplet[1])) / (
                       (x_triplet[2] - x_triplet[0]) * (x_triplet[2] - x_triplet[1]))


if __name__ == '__main__':
    main()
