from numpy import linspace
from math import factorial
from itertools import zip_longest


def gridspace(a, b, n, d=1):
    return (linspace(a, b, endpoint=True, num=n),) * d


def diagonal_transpose(triangularMatrix):
    return [[triangularMatrix[i - j][j]
             for j in range(i, 0 - 1, -1)]
            for i in range(len(triangularMatrix))]


def transpose(matrix):
    return zip_longest(*matrix)


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def sum_tuple(*tuples):
    return tuple(map(sum, zip(*tuples)))


def scalar_tuple_product(a, b):
    return tuple(map(lambda x: x * a, b))
