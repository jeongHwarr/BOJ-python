'''
https://www.acmicpc.net/problem/1026
(Input)
5
1 1 1 6 0
2 7 8 3 1

(Output)
18
'''

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)

    sum=0
    for i in range(len(A)):
        sum+=A[i]*B[i]
    print(sum)


