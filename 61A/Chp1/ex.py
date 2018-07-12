from operator import floordiv, mod
from math import pi, sqrt

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def newton_update(f, df):
    print('newton update')

    def update(x):
        return x - f(x) / df(x)

    return update


def power(x, n):
    print('power')
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def root(n, a):
    print('root')

    def f(x):
        print('fx')
        return power(x, n) - a

    def df(x):
        print('df')
        return n * power(x, n - 1)

    return find_zero(f, df)


def improve(update, close, guess=1, max_update=100):
    print('improve')
    k = 0
    while not close(guess) and k < max_update:
        guess = update(guess)
        k = k + 1
        print('k', k)
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def sum_consecutive(f):
    total = 0
    k = 0
    while k <= f:
        total += k
        k += 1
    return total


def collatz_sequence(n):
    hail_len = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        hail_len += 1
    return hail_len


def collatz_sequence_length(n):
    return collatz_sequence(n)


def every_longer_collatz():
    longest_length = 0
    longest_number = 1
    n = 1
    while True:
        current_length = collatz_sequence_length(n)
        if current_length > longest_length:
            longest_length = current_length
            longest_number = n
            print(n)
        n += 1


def sum_divisors(n):
    i = 1
    sum_div = 0
    while i <= n:
        if n % i == 0:
            sum_div += i
        i += 1
    return sum_div


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
