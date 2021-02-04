# Search & Sorting-01
# https://www.acmicpc.net/problem/1920
"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
def binary_search(target_list, number):
    index = int(len(target_list)/2)
    if index<0 or index==len(target_list):
        return 0
    target = target_list[index]
    if (number > target) and index<len(target_list)-1:
        return binary_search(target_list[index+1:], number)
    elif number < target:
        return binary_search(target_list[:index], number)
    elif number==target:
        return 1
    else:
        return 0

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
        print(find)