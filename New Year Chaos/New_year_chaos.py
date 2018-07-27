

def numOfBribes():

    # variables
    n = int(input())
    q = [int(x) for x in input().split()]
    lastIndex = len(q) - 1
    moves = 0
    swap = False

    # Check if too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            return 'Too chaotic'

    # figure out number of moves
    for i in range(len(q)):
        for j in range(lastIndex):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                moves += 1
                swap = True
        
        # check if any swap have accured - if not it means the queue is sorted
        if swap:
            swap = False
            lastIndex -= 1
        else:
            return moves
    return moves
        
        
for _ in range(int(input())):
    print(numOfBribes())
