from typing import List


def asterisks_right_to_left(x: str) -> str:
    i = len(x) - x.count('*') - 1
    if i <= 0:
        return '*'
    else:
        temp = list(x)
        temp[i] = '*'
        return ''.join(temp)


def get_list_generalizer(g: List[str]):
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
