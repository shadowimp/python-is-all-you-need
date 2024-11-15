二分查找（也称为折半查找）的基本思路是这样的：

1. **初始化**: 确定搜索区间，通常是一个有序数组的起始索引（`left`）和结束索引（`right`）。
2. **检查中间**: 计算中间索引 `mid = (left + right) // 2`，然后检查中间元素是否等于目标值。
3. **缩小范围**:
   - 如果中间元素等于目标值，搜索成功，返回索引 `mid`。
   - 如果中间元素小于目标值，则目标值应在右半部分（`left = mid + 1`），缩小搜索区间至右半部分。
   - 如果中间元素大于目标值，则目标值应在左半部分（`right = mid - 1`），缩小搜索区间至左半部分。
4. **重复步骤2和3**，直到找到目标值或搜索区间为空（即 `left > right`）。
5. **未找到**: 如果搜索区间为空，说明目标值不在数组中，返回一个特定值表示未找到，通常返回-1。

这种方法效率高，时间复杂度为O(log n)，其中n是数组的长度。但前提是数组必须是有序的。



```python
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
```

