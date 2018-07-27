
A = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    A.append(arr_t)
    
smax = -9 * 7

for row in range(len(A) - 2):
    for column in range(len(A[row]) - 2):
        s = A[row][column] + A[row][column+1] + A[row][column+2] + A[row+1][column+1] + A[row+2][column] + A[row+2][column+1] + A[row+2][column+2]
        smax = max(s, smax)
        
print(smax)