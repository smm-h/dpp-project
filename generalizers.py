def asterisks_right_to_left(x: str) -> str:
    i = len(x) - x.count('*') - 1
    if i <= 0:
        return '*'
    else:
        temp = list(x)
        temp[i] = '*'
        return "".join(temp)
