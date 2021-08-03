"""
https://www.acmicpc.net/problem/1874

(Input)
8
4
3
6
8
7
5
2
1

(Output)
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
"""
if __name__ == '__main__':
    n = int(input())
    target=[]
    for _ in range(n):
        target.append(int(input()))

    stack=[]
    answer = []
    target_idx=0

    for number in range(1,n+1):
        stack.append(number)
        answer.append('+')
        while(len(stack)!=0 and stack[-1]==target[target_idx]):
            stack.pop()
            if target_idx<len(target)-1: target_idx+=1
            answer.append('-')

        if len(stack)!=0 and stack[-1]>target[target_idx]:
            answer = []
            answer.append('NO')
            break

    if target_idx!=len(target)-1:
        answer=[]
        answer.append('NO')

    for i in range(len(answer)):
        print(answer[i])

