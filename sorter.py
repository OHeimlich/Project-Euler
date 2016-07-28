def bitonic_sorter(numbers):
    n = len(numbers)
    if n ==1:
        return numbers
    for i in (range(n)/2)+1:
        if numbers[i] > numbers[n-i]:
            numbers[i], numbers[n-i] = numbers[n-i], numbers[i]



def RHC(numbers):
    pass


def sorter(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 2:
        if numbers[0] <= numbers[1]:
            return numbers
        else:
            return [numbers[1], numbers[0]]
    return merger(sorter(numbers[:len(numbers)/2], sorter(numbers[len(numbers)/2:])))


def merger(l1, l2):
    pass

