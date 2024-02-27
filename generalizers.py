from typing import List


def asterisks_right_to_left(x: str) -> str:
    i = len(x) - x.count('*') - 1
    if i <= 0:
        return '*'
    else:
        temp = list(x)
        temp[i] = '*'
        return ''.join(temp)


def age_generalizer(x: str) -> str:
    if '-' not in x:
        k = 5
    else:
        a, b = x.split('-')
        a, b = int(a), int(b)
        k = (b - a) * 2
        x = (a + b) / 2

    a = int(int(x) / k) * k
    return f'{a}-{a + k}'


def make_list_generalizer(g: List[str]):
    # for faster inclusion checks
    s = set(g)

    def generalizer(x: str) -> str:
        if x in s:
            i = g.index(x)
            if i + 1 == len(g):
                return '*'
            else:
                return g[i + 1]
        else:
            return g[0]

    return generalizer
