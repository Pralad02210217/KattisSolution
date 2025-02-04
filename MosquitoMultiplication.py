import sys
try:
    while True:
        M,P,L,E,R,S,N = map(int, input().split())
        for i in range(N):
            tempM = M
            tempP = P
            tempL = L
            L = tempM * E
            P = tempL // R
            M = tempP // S
        print(M)
        
except EOFError:
    sys.exit()