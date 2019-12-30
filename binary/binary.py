def binary_search(list, item):
    """
    이진 탐색 함수
    :param list: 정렬된 리스트
    :param item: 찾고자하는 숫자
    :return:
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid -1
        else:
            low = mid + 1
    return None

# 함수 테스트
my_list = [1, 3, 5, 7, 9]
print (binary_search(list= my_list, item= 3))
