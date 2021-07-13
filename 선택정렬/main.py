def selection_sort(list):

    for h in range(len(list)):
        # 현재 비교하는 가장 작은 인덱스 값
        min = list[h]

        # 바꿔야 하는 최소값 인덱스 찾기
        for i in range(h, len(list)):
            if min > list[i]:
                min = list[i]
                temp = i

        # 최솟값과 현재 비교하는 가장 작은 인덱스 자리를 교환한다.
        list[h], list[temp] = min, list[h]

    return list