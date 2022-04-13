
numbers: list = [1, 5, 3, 7, 1, 9, 0]


def bubble_sort(num) -> list:
    count = len(num)-1
    while count > 0:
        for x in range(len(num)-1):
            maxi = num[x]
            if num[x] > num[x+1]:
                mini = num[x+1]
                num[x] = mini
                num[x+1] = maxi
        count -= 1
    return num


print(bubble_sort(numbers))
