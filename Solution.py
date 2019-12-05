"""
Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input:
First line contains 2 space separated integers, N - total rows, M - total columns.
Each of the next N lines will contain M space separated integers.

Output:
Print M lines each containing N space separated integers. 
"""
L = input()
N = int(L.split()[0])
M = int(L.split()[1])

C = []
for x in range(0, N):
    B = input()
    R = []
    for j in range(0, M):
        R.append(B.split()[j])
        
    C.append(R)

 
rez = [[C[j][i] for j in range(len(C))] for i in range(len(C[0]))] 
D = ""
for row in rez:
    for r in row:
        D += r + " "
    D += "\n"

print(D)
