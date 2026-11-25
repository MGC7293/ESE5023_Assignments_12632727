"""
Created on Mon Oct 5 2026

@author: 12632727-LI Tianzhu
"""
#1 Flowchart
import random
def Print_values(a, b, c):
    if a > b:
        if b > c:
            print(a, b, c)
        else:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if b > c:
            if a > c:
                print(a, c, b)
            else:
                print(c, a, b)
        else:
            print(c, b, a)
if __name__ == "__main__":
    random.seed(0)
    for _ in range(5):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        print("a = %3d, b = %3d, c = %3d -> " % (a, b, c), end="")
        Print_values(a, b, c)


#2 Matrix multiplication
import numpy as np
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))

def Matrix_multip(M1, M2):
    rows = len(M1)
    cols = len(M2[0])
    inner = len(M2)
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s = 0
            for k in range(inner):
                s = s + M1[i][k] * M2[k][j]
            result[i][j] = s
    return result

if __name__ == "__main__":
    np.random.seed(0)
    M1 = np.random.randint(0, 51, size=(5, 10))
    M2 = np.random.randint(0, 51, size=(10, 5))
    print("M1 (5x10):")
    print(M1)
    print("M2 (10x5):")
    print(M2)

    result = Matrix_multip(M1.tolist(), M2.tolist())
    result_arr = np.array(result)
    print("M1 * M2 (by Matrix_multip):")
    print(result_arr)
    print("Matches numpy dot product:", 
          np.array_equal(result_arr, np.dot(M1, M2)))


#3 Pascal triangle
def Pascal_triangle(k):
    line = [1]
    for _ in range(1, k):
        line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
    return line


def print_line(k):
    line = Pascal_triangle(k)
    print("Pascal_triangle(%d): %d numbers" % (k, len(line)))
    for i in range(0, len(line), 10):
        print(line[i:i + 10])
    print("Sum check = 2^(k-1):", sum(line), "==", 2 ** (k - 1))
    print()


if __name__ == "__main__":
    print_line(100)
    print_line(200)


#4 Add or double
import random


def Least_moves(x):
    moves = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = x - 1
        moves = moves + 1
    return moves


if __name__ == "__main__":
    print("Least_moves(2) =", Least_moves(2))
    print("Least_moves(5) =", Least_moves(5))
    random.seed(1)
    x = random.randint(1, 100)
    print("Random x =", x, "-> Least_moves(%d) = %d" % (x, Least_moves(x)))


#5 Dynamic programming
from itertools import product

import matplotlib.pyplot as plt

DIGITS = "123456789"


def evaluate(digits, ops):
    total = 0
    sign = 1
    num = int(digits[0])
    for i, op in enumerate(ops):
        if op == "":
            num = num * 10 + int(digits[i + 1])
        else:
            total = total + sign * num
            num = int(digits[i + 1])
            sign = 1 if op == "+" else -1
    total = total + sign * num
    return total


def expression_str(digits, ops):
    s = digits[0]
    for i, op in enumerate(ops):
        s = s + op + digits[i + 1]
    return s


def Find_expression(x):
    count = 0
    for ops in product(("+", "-", ""), repeat=8):
        if evaluate(DIGITS, ops) == x:
            print(expression_str(DIGITS, ops) + "=" + str(x))
            count = count + 1
    print("Total solutions for %d: %d" % (x, count))


if __name__ == "__main__":
    x = 50
    print("Find_expression(%d):" % x)
    Find_expression(x)

    Total_solutions = [0] * 101
    for ops in product(("+", "-", ""), repeat=8):
        v = evaluate(DIGITS, ops)
        if 1 <= v <= 100:
            Total_solutions[v] = Total_solutions[v] + 1

    plt.figure(figsize=(10, 5))
    plt.bar(range(1, 101), Total_solutions[1:], color="#2a9d84")
    plt.xlabel("target value i")
    plt.ylabel("number of solutions")
    plt.title("Total_solutions for i = 1..100")
    plt.savefig("PS1_5_Total_solutions.png", dpi=150)

    max_count = max(Total_solutions[1:])
    min_count = min(Total_solutions[1:])
    max_vals = [i for i in range(1, 101) if Total_solutions[i] == max_count]
    min_vals = [i for i in range(1, 101) if Total_solutions[i] == min_count]
    print("Maximum Total_solutions = %d, at i = %s" % (max_count, max_vals))
    print("Minimum Total_solutions = %d, at i = %s" % (min_count, min_vals))
