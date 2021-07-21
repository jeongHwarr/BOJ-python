"""
https://www.acmicpc.net/problem/9012

(Input)
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

(Output)
NO
NO
YES
NO
YES
NO
"""

if __name__ == '__main__':
    T = int(input())
    answer=[]
    for t in range(T):
        valid=True
        stack=[]
        bracket = list(input())
        for cur_char in bracket:
            if cur_char=='(':
                stack.append('(')
            elif cur_char==')':
                if len(stack)==0 or stack[-1]!='(':
                    valid=False
                    break
                stack.pop()
        if valid and len(stack)==0:
            answer.append('YES')
        else:
            answer.append('NO')

    for t in range(T):
        print(answer[t])

