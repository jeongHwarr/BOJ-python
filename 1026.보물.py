'''
https://www.acmicpc.net/problem/1026
(Input)
5
1 1 1 6 0
2 7 8 3 1

(Output)
18
'''

from collections import OrderedDict
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B_dict={}

    for idx, number in enumerate(B):
        B_dict[idx]=number


    sorted_B = OrderedDict(sorted(B_dict.items(), key=lambda item:item[1]))

    sorted_A = sorted(A,reverse=True)

    new_A=[0]*len(sorted_A)
    for from_idx, to_idx in enumerate(sorted_B.keys()):
        new_A[to_idx]=sorted_A[from_idx]

    sum=0
    for i in range(len(new_A)):
        sum+=new_A[i]*B[i]
    print(sum)


