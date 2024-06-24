# 这个Python函数实现了二分查找算法，它在已排序的列表中查找指定的目标值。如果找到目标值，返回其在列表中的索引；如果列表中不存在该值，则返回-1。
def binary_search(arr, target):
    """
    二分查找函数
    :param arr: 排序好的列表
    :param target: 查找的目标值
    :return: 目标值在列表中的索引，如果不存在则返回-1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 3))

