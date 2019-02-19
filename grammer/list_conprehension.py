a = [2, 6, 7, 8, 9]
vec = [num for num in a if num % 2 == 0]

vec = []
for num in a:
    if num % 2 == 0:
        vec.append(num)
