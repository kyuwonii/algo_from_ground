
def select_sort(list):
    for i in range(0,len(list)):
        max = list[i]

        for j in range(max):
            if list[max] < list[j]:
                temp = list[j]
                list[j] = list[max]
                list[max] = temp

    return list
