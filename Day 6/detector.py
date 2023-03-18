from collections import deque
 
def get_n_char_marker(data:str, n:int):
    current_n_char = deque([data[0]]*n) #initlized to the first char of data so the earliest possible find is at char count n
    for count, ch in enumerate(data, 1):
        current_n_char.popleft()
        current_n_char.append(ch)
        if len(current_n_char) == len(set(current_n_char)):
            return count