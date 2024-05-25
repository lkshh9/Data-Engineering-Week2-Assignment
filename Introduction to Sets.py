def average(array):
    set1 = set(array)
    n = len(set1)
    sum = 0
    for i in set1:
        sum += i

    avg = sum / n
    return avg
