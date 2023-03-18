from collections import deque
import detector
with open ('Day 6/input.txt') as input:
    data = input.readline()

print(detector.get_n_char_marker(data, 4))
