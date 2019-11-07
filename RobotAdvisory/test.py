import json

data = open('/home/am/pythom/data.json').josn()
def find_two_sum(numbers, target_sum):
    li = []
    temp = []
    for j, i in enumerate(numbers):
        for k in range(j + 1, len(numbers)):
            if i + numbers[k] == 10:
                if len(temp) == 0:
                    temp.append(i)
                    temp.append(numbers[k])
                    li.append(f"{j} and {k} or ({k} and {j}) as {i} + {numbers[k]} = {i + numbers[k]}")
                if numbers[k] not in temp:
                    temp.append(i)
                    temp.append(numbers[k])
                    li.append(f"{j} and {k} or ({k} and {j}) as {i} + {numbers[k]} = {i + numbers[k]}")
    return tuple(li)


print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
