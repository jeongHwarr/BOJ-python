'''
https://www.acmicpc.net/problem/1966
(Input)
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

(Output)
1
2
5
'''

from collections import deque

def print_queue(N, target, prioiry):
    dequeue = deque()

    # dequeue 만들기 (prioiryt, target)
    for i in range(N):
        if i==target:
            elem_list = [prioiry[i], 1]
        else:
            elem_list = [prioiry[i],0]
        dequeue.append(elem_list)
    #print(dequeue)

    prioiry = sorted(prioiry, reverse=True)
    answer=0
    while(len(dequeue)):
        if dequeue[0][0]==prioiry[answer]:
            pop_elem = dequeue.popleft()
            answer+=1
            if pop_elem[1]==1:
                return answer
        else:
            dequeue.rotate(-1)
    return answer

def main():
    T = int(input()) # 테스트 개수

    for t in range(T):
        N, target = map(int, input().split())
        priority = list(map(int, input().split()))
        print(print_queue(N, target, priority))

if __name__ == '__main__':
    main()