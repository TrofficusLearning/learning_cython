def sum(int n):
    cdef int sum, i 
    sum = i = 0
    while i < n:
        sum += i
        i += 1
    return sum
