def sum_lst(lst):
    if lst == []:
        return 0
    return lst.pop() + sum_lst(lst)


def comprehension(lst, f, pred):
    if lst == []:
      return []
    first = [f(lst[0])] if pred(lst[0]) else []
    return first + comprehension(lst[1:], f, pred)


def balanced(s, depth=0):
    if not s:
        return depth == 0
    if depth < 0:
        return False
    if s[0] == '(':
        return balanced(s[1:], depth + 1)
    if s[0] == ')':
        return balanced(s[1:], depth - 1)
    else:
        return balanced(s[1:], depth)


def multiply(m, n):
    if m == 0:
        return 0
    elif m == 1:
        return n
    else:
        return n + multiply(m-1, n)


def countdown(n):
    if n == 1:
        return 1
    print(n)
    return countdown(n - 1)


def countup(n, count):
    if count == n:
        return n
    print(n)
    return countup(n, count + 1)


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last