
numbers: list = [2, 5, 3, 7, 1, 9, 0]

def selection_sort(num)->list:
    for x in range(len(num)):
        minimum = num[x]
        index = x
        select = num[x]
        for value in range(index, len(num)):
            if minimum > num[value]:
                minimum = num[value]
                index = value
        if minimum != select:
            num[x] = minimum
            num[index] = select
    return num

print(selection_sort(numbers))
