def binary_search(element, some_list):
    # 코드를 작성하세요.
    
    start = 0
    end = len(some_list) - 1
    
    while start <= end :
        mid_number = some_list[(start + end) // 2]
        
        if element == mid_number :
            return some_list.index(mid_number)
        elif element > mid_number :
            start = mid_number + 1
        else : 
            end = mid_number - 1
           
    return None   



print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))