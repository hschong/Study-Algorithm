def find_idx_for_min(list):    min = list[0]    min_idx = 0    length = len(list)    for i in range(1, length):        if min > list[i]:            min = list[i]            min_idx = i    return min_idxdef sel_sort(list):    new_list = []    for i in range(1, len(list)):        min_idx = find_idx_for_min(list)        new_list.append(list.pop(min_idx))    new_list.append(list.pop())    return new_listdef selection_sort(list):    length = len(list)    for i in range(0, length-1):        idx_for_min = i        for j in range(i+1, length):            if list[j] < list[idx_for_min]:                idx_for_min = j        list[i], list[idx_for_min] = list[idx_for_min], list[i]data1 = [5, 3, 6, 2, 10, 15, 9, 1, 11, 7]data2 = [5, 3, 6, 2, 10, 15, 9, 1, 11, 7]print(data1)print(sel_sort(data1))print(data2)selection_sort(data2)print(data2)