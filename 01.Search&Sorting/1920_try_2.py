# Search & Sorting-01
# https://www.acmicpc.net/problem/1920
"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
if __name__ == '__main__':
    # reference
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)

    # input
    M = int(input())
    B = list(map(int,input().split()))

    find_dict = {}
    for number in B:
        target_list = A
        find=-1
        if number in find_dict:
            find = find_dict[number]
        else:
            while(start<end):
                index = int(len(target_list) / 2)
                if index < 0 or index == len(target_list):
                    find=0
                    break
                target = target_list[index]
                if (number > target) and index<len(target_list)-1:
                    target_list=target_list[index+1:]
                elif number < target:
                    target_list=target_list[:index]
                elif number==target:
                    find=0
                    break
                else:
                    find=0
                    break
            find_dict[number]=find
        print(find)
