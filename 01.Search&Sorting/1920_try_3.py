# Search & Sorting-01
# https://www.acmicpc.net/problem/1920
"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
def binary_search(target_list, number):
    start = 0
    end = len(target_list)-1
    while(start<=end):
        mid = int((end-start)/2)+start
        if number == target_list[mid]:
            return 1
        elif number > target_list[mid]:
            start=mid+1
        elif number < target_list[mid]:
            end=mid-1

if __name__ == '__main__':
    # reference
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)

    # input
    M = int(input())
    B = list(map(int,input().split()))

    for number in B:
        find = binary_search(A, number)
        if find==None: find=0
        print(find)