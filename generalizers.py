from typing import List, Dict


def asterisks_right_to_left(x: str) -> str:
    x = str(x)
    i = len(x) - x.count('*') - 1
    if i <= 0:
        return '*'
    else:
        temp = list(x)
        temp[i] = '*'
        return ''.join(temp)


def age_generalizer(x: str) -> str:
    x = str(x)
    if '-' not in x:
        k = 5
    else:
        a, b = x.split('-')
        a, b = int(a), int(b)
        k = (b - a) * 2
        x = (a + b) / 2

    a = int(int(x) / k) * k
    return f'{a}-{a + k}'


def make_taxonomy_generalizer(t: Dict[str, str]):

    def generalizer(x: str) -> str:
        x = str(x)
        if x in t:
            return t[x]
        else:
            return '*'

    return generalizer
